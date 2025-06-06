# Adding Writing Tools support to a custom UIKit view

**Framework**: UIKit

Add Writing Tools support, including support for inline replacement animations, to your custom iOS views that contain text.

#### Overview

If you don’t use a [`UITextView`](uitextview.md) or [`UITextField`](uitextfield.md) object in your app, you can still add Writing Tools support to other views that contain text. You might use this support when you prefer not to use the standard text views. For example, you might use it if you build your own text view using TextKit or your own proprietary text engine. The UIKit API for this support gives you access to the same Writing Tools features available in the system views, including the ability to animate changes to the text in your view.

When a person triggers the Writing Tools UI from your custom view, UIKit works with your view to evaluate the relevant text and incorporate changes. You specify the type of Writing Tools experience you want for your view. The complete experience animates changes to your view’s content directly, working with your view to create those animations. The limited experience displays changes in the Writing Tools UI, and only incorporates the final changes back into your view’s text storage. All of these interactions happen with the help of the [`UIWritingToolsCoordinator`](uiwritingtoolscoordinator.md) object you attach to your view.

##### Add a Writing Tools Coordinator to Your View

A [`UIWritingToolsCoordinator`](uiwritingtoolscoordinator.md) object manages interactions between your view and the Writing Tools feature. In iOS, this object is a type of [`UIInteraction`](uiinteraction.md) object, and you attach to your view only when you want to support Writing Tools. To manage your view-specific behavior, you provide a delegate object when setting up the coordinator. Your delegate provides Writing Tools with initial text to evaluate, incorporates changes, provides proofreading marks, and provides preview objects to use during animations.

Attach a coordinator object to your view, typically when creating and configuring that view. Supply a delegate object that adopts the [`UIWritingToolsCoordinator.Delegate`](uiwritingtoolscoordinator/delegate-swift.protocol.md) protocol and has access to your view’s text content and layout information. The following example shows an extension to a custom view that creates the coordinator and initializes it with the view itself. The custom method checks to see if Writing Tools is available before creating a coordinator object and adding it to the view.

```swift
class MyTextView : UIView {
    var coordinator: UIWritingToolsCoordinator?

   //…
}

extension MyTextView : UIWritingToolsCoordinator.Delegate {

    func configureWritingTools() {
        guard UIWritingToolsCoordinator.isWritingToolsAvailable else { return }
        guard coordinator == nil else { return }
        
        coordinator = UIWritingToolsCoordinator(delegate:self)
        addInteraction(coordinator!)
    }
   //…
}
```

The presence of a coordinator object on your view causes UIKit to enable Writing Tools support for that view. When someone interacts with your view’s contextual menu, UIKit automatically adds a command to that menu to launch Writing Tools.

For a complete list of delegate methods you must implement to support Writing Tools, see [`UIWritingToolsCoordinator.Delegate`](uiwritingtoolscoordinator/delegate-swift.protocol.md).

##### Configure Your Views Writing Tools Behavior

When setting up Writing Tools for your view, configure your coordinator’s [`preferredBehavior`](uiwritingtoolscoordinator/preferredbehavior.md) property with the types of interactions you support. Writing Tools offers different levels of integration with your view’s content, which also affects how much work you need to do to support the feature. With the complete experience, you provide UIKit with more information so that it can make changes directly in your view. The limited experience pushes more interactions into the Writing Tools UI, giving you a less integrated experience, but one that’s easier to implement.

At configuration time, you also specify the types of text content your view supports using your coordinator’s [`preferredResultOptions`](uiwritingtoolscoordinator/preferredresultoptions.md) property. The models that Writing Tools uses to evaluate your text can generate plain or formatted text. Writing Tools supports all types of output by default, but you can limit it to specific types as needed.

The following code updates the previous example method, and adds some preferred behaviors for the coordinator object. In addition to wanting the inline experience for Writing Tools interactions, the method requests that the system generate rich text and optional list-based content. Providing a specific list of result options tells Writing Tools to generate only that type of content. You might provide this information if your view doesn’t support specific types of content, like tables.

```swift
func configureWritingTools() {
    guard UIWritingToolsCoordinator.isWritingToolsAvailable else { return }
    guard coordinator == nil else { return }

    coordinator = UIWritingToolsCoordinator(delegate:self)
    coordinator?.preferredBehavior = .complete
    coordinator?.preferredResultOptions = [.richText, .list]
    addInteraction(coordinator!)
}
```

The availability of Writing Tools depends on the current device, its operating system, and its readiness to execute requests. On devices with appropriate hardware, some Writing Tools features operate locally after the system downloads the required models. However, more complex requests require a network connection so the system can use [`Private Cloud Compute`](https://developer.apple.comhttps://security.apple.com/documentation/private-cloud-compute) to evaluate the provided text.

##### Supply Your Views Text for Evaluation

When someone starts Writing Tools in your view, the system asks your delegate to provide the text to evaluate. Depending on what the person wants to do, Writing Tools might ask for only the selected text or it might ask for all of your view’s text. For example, they might want to proof only the currently selected text, or they might want to proofread all of the text in your view. You provide that text from your delegate inside a context object.

A [`UIWritingToolsCoordinator.Context`](uiwritingtoolscoordinator/context.md) object is a data object that you fill with the requested text. Context objects provide the common ground that you and Writing Tools use to communicate throughout a single operation. For each request, you create one context object for each text-storage object that has text for Writing Tools to consider. Most views have only one text-storage object and therefore create only one context object. However, a view that uses multiple subviews to manage different parts of its content might assign separate text- storage objects to each subview. In that scenario, you create one context object for each subview that contains the requested text.

To request your view’s context object, the coordinator calls your delegate’s [`writingToolsCoordinator(_:requestsContextsFor:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:).md) method. Use the parameters of that method to determine if Writing Tools wants all of your view’s text or only some of it. The following example creates a single context object with either the currently selected text or the view’s full text. After creating the context, the custom `storeContexts` method saves a reference to the context for subsequent tasks.

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsContextsFor scope: UIWritingToolsCoordinator.ContextScope,
        completion: @escaping ([UIWritingToolsCoordinator.Context]) -> Void) {

    // Store the created contexts for the completion handler.
    var contexts = [UIWritingToolsCoordinator.Context]()
                
    switch scope {
    case .userSelection:
        let context = getContextObjectForSelection()
        contexts.append(context)
        break
            
    case .fullDocument:
        let context = getContextObjectForFullDocument()
        contexts.append(context)
        break

    case .visibleArea:
        let context = getContextObjectForVisibleArea()
        contexts.append(context)
        break

    default:
        break
    }
        
    // Save references to the contexts for later delegate calls.
    storeContexts(contexts)
        
    // Deliver the contexts to Writing Tools.
    completion(contexts)
}
```

When specifying only a subset of your view’s text, provide some of the surrounding text to give Writing Tools additional content for its evaluation. As a general principle, include whole paragraphs of text in the context object, not just the currently selected text. Use the context object’s range value to identify the portion of the overall text that Writing Tools requested. For example, if you fill a context object with the current text selection and some of the surrounding text, use the context object’s [`range`](uiwritingtoolscoordinator/context/range.md) property to specify the location of the selected text in that object.

After you create a context object, cache any additional information that you need to map the text in your context object to the text in your view’s text storage. You need to know where the content for each context object starts, in order to update your text storage later. One option is to create a dictionary that maps the context object’s identifier to the starting location of its text in your text storage. You can use that value to adjust any context-specific ranges that Writing provides you later.

The following example shows a method that the delegate uses to create a context object for the current text selection. The method calls the custom `getSelectedTextToEvaluate` function, which returns an expanded version of the text that includes both the selection and some of the surrounding text. The method also returns the starting location of that expanded text in the view’s text storage. Because the text selection is now in the middle of the text, the method initializes the context object with a range that provides the location of only the selected text, relative to the start of `textToEvaluate`. The method saves the actual starting location in a dictionary variable, mapping the value to the context’s unique identifier.

```swift
var startingLocationsForContexts = [UUID : Int]()

func getContextObjectForSelection() -> UIWritingToolsCoordinator.Context {
    // Get the text to evaluate, which includes the text selection and some
    // of the surrounding text. The method returns (NSAttributedString, Int),
    // which represents the text itself, and the starting location of that
    // text in the view's text storage.
    let (textToEvaluate, startLocation) = getSelectedTextToEvaluate()

    // Get the NSRange for the text selection, relative to the text storage.
    let textSelectionRange = getTextSelectionRange()
    var contextRange = textSelectionRange
        
    // The view guarantees that startLocation is less than or equal to the
    // selection range. Adjust contextRange so that location 0 corresponds
    // to the first character in textToEvaluate. Keep the length the same.
    contextRange.location = textSelectionRange.location - startLocation
        
    // Create the new context object.
    let context = UIWritingToolsCoordinator.Context(attributedString: textToEvaluate, range: contextRange)
    
    // Save the starting location of the text, relative to the text storage.
    startingLocationsForContexts[context.identifier] = startLocation
    
    return context
}
```

After you create a context object, you can use its unique identifier as a key for saving other data. The context objects you create remain in existence for the duration of the current Writing Tools operation. If the person rejects the current changes and starts a new operation, Writing Tools asks you for a new set of context objects.

##### Incorporate Writing Tools Changes Into Your View

After evaluating your view’s text, Writing Tools delivers any suggested changes to your delegate object. If your view adopts the limited experience, Writing Tools waits until the person accepts any changes before delivering them to your view. If you adopt the complete experience, Writing Tools delivers the changes before the person accepts them. If the person later rejects the changes, Writing Tools delivers a new set of changes that restore your view’s original text.

In your delegate’s [`writingToolsCoordinator(_:replace:in:proposedText:reason:animationParameters:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:replace:in:proposedtext:reason:animationparameters:completion:).md) method, incorporate the specified change into your view’s text storage. Writing Tools calls this method for each distinct change it needs to make, and it might call the method multiple times with different range values for the same context object. The following simple example validates the provided range information and validates the view’s own cached information for the context object. If everything is valid, the method then calculates the correct range of text to replace and creates a transaction to perform the replacement. Before returning, the method executes the provided completion handler with the text it incorporated, if any.

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        replace range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        proposedText replacementText: NSAttributedString, 
        reason: UIWritingToolsCoordinator.TextReplacementReason, 
        animationParameters: UIWritingToolsCoordinator.AnimationParameters?, 
        completion: @escaping (NSAttributedString?) -> Void) {
        
    // Make sure there's a valid starting location in the text storage.
    guard let startingLocation = startingLocationsForContexts[context.identifier] 
        else { completion(nil); return }
    guard let textStorage = textContentStorage.textStorage else { completion(nil); return }

    // Determine the correct location in the text storage.
    let adjustedRange = NSRange(location: startingLocation + range.location, length: range.length)
        
    // Update the view’s NSTextContentManager using a transaction.
    textContentStorage.performEditingTransaction {
        textStorage.replaceCharacters(in: adjustedRange, with: replacementText)
    }
    
    completion(replacementText)
}
```

After each replacement operation, update other parts of your app as needed to account for the change. An [`NSTextContentManager`](nstextcontentmanager.md) object automatically generates the required layout updates when you make changes using a transaction. If you need to update other parts of your interface, initiate those changes from your [`writingToolsCoordinator(_:replace:in:proposedText:reason:animationParameters:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:replace:in:proposedtext:reason:animationparameters:completion:).md) method. For example, you might update a view that displays the current character count for your document. Check the `reason` parameter to determine when Writing Tools is making changes interactively, and use the provided animation parameters object to create the actual animations.

##### Update Your Views Selected Text

When working on your view’s selected text, Writing Tools updates the text selection to account for any text updates. Use your delegate’s [`writingToolsCoordinator(_:select:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:select:in:completion:).md) method to update the selected text in your view. The method delivers an array of range values to allow for views to create discontiguous selections. If your view supports only a continuous range of selected characters, update your view’s selection based on the first element in the `ranges` array.

When implementing your delegate method, remember to update range values to account for offset to the start of the text in your context object. The following example creates an adjusted set of ranges by adding the starting location recorded at the start of the operation for the context object. It then passes that information to the view’s text engine to highlight the appropriate ranges of text.

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        select ranges: [NSValue], 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping () -> Void) {
        
    guard let startingLocation = startingLocationsForContexts[context.identifier] 
              else { completion(); return }
    var adjustedRanges = [NSRange]()
        
    for value in ranges {
        let range = value.rangeValue
        let newRange = NSRange(location: startingLocation + range.location, length: range.length)
        adjustedRanges.append(newRange)
    }

    // Highlight the specified text in the view.
    selectTextInDocument(adjustedRanges)
    completion()
}
```

##### Generate Preview Images for Inline Animated Changes

When you choose the complete Writing Tools experience for your view, the system animates changes to your content directly in your view. The system creates animations when Writing Tools starts evaluating your text, when it removes old text, and when it inserts new text. Because the animations involve your content, you must help the system create them. At appropriate times, the coordinator asks your delegate object to perform the following tasks:

1. Create a preview image of a specific portion of your content.
2. Hide that content when the animation starts.
3. Show the content again when the animation finishes.

To create a preview image of your text, use your layout manager and a [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) to generate the image in your delegate’s [`writingToolsCoordinator(_:requestsPreviewFor:of:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md) method. Use your layout manager to get the frame rectangle that surrounds the specified text, and configure your image renderer with the size of that rectangle. In your rendering code, configure a clipping path to limit drawing to the area that contains only the specified text, and render that text onto a clear background.

The following example shows an implementation of the [`writingToolsCoordinator(_:requestsPreviewFor:of:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md) method that creates a preview image for the view’s text. The method relies on the view’s layout manager to get the text rectangles that surround each line of text in the specified range. It also uses the layout manager to draw the text within the block of the graphics renderer. The image renderer generates an image with the rendered text, which the method places in an image view and uses to create a [`UITargetedPreview`](uitargetedpreview.md) object. Setting the frame rectangle of the image view tells Writing Tools where to place that image in the overall text view. When creating animations, Writing Tools applies the required visual effects to the provided image view instead of to the text itself.

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsPreviewFor textAnimation: UIWritingToolsCoordinator.TextAnimation, 
        of range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping (UITargetedPreview?) -> Void) {
        
    let textRange = MyTextRange(range)         // Create the view's custom subclass of NSTextRange.
    let textRects = getTextRectangles(range)   // Returns an array of NSValue<NSRect*>.

    if !textRange.isEmpty {
        // Get the frame rectangle that encloses the text.
        let textFrame = unionRect(for: textRects.map({$0.cgRectValue}))
            
        // Create the image renderer and render the image.
        let renderer = UIGraphicsImageRenderer(bounds: textFrame)
        let image = renderer.image { context in
            // Limit drawing to the text rectangles.
            context.cgContext.clip(to: textRects.map({$0.cgRectValue}))
                
            // Draw the specified range of text using the view's layout manager.
            drawTextInRange(range)
        }
        // Create an image view and set its frame to match the area with the text.
        let imageView = UIImageView(image:image)
        imageView.frame = textFrame
            
        // Create the targeted preview.
        let parameters = UIPreviewParameters(textLineRects: 
                       textRects.map({NSValue(cgRect: $0.cgRectValue)}))
        let target = UIPreviewTarget(container: self, center: self.center)
        let preview = UITargetedPreview(view: imageView, parameters: parameters, target: target)
            
        completion(preview)
    }
    else {
        completion(nil)
    }
}
```

In addition to providing the initial image, use the [`writingToolsCoordinator(_:prepareFor:for:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:).md) method to hide the specified range of text in your view. UIKit inserts the image view from your [`UITargetedPreview`](uitargetedpreview.md) object into the same part of your view that contains the hidden text. Placement of the image view is important, which is why you must set its frame rectangle to the precise location of the text in your view. When the animations finish, Writing Tools calls the [`writingToolsCoordinator(_:finish:for:in:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md) method so you can show the text in the specified range again.

##### Create Proofreading Marks for Your Content

If someone chooses a proofreading option, Writing Tools evaluates your view’s text and asks you to provide proofreading marks to decorate the view. For each mark, Writing Tools asks you to provide a Bézier path that underlines the text in a particular range. The following example uses the view’s layout manager to get the bounding rectangles for the specified range of text. It then flattens those rectangles to create a line shape underneath the text and passes the resulting paths to the completion handler. The code creates separate shapes for each rectangle to account for situations where a proofreading mark extends onto multiple lines of text.

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsUnderlinePathsFor range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping ([UIBezierPath]) -> Void) {

    let textRects = getTextRectangles(range)   // Returns an array of NSValue<NSRect*>.
        
    var paths = [UIBezierPath]()
    for rect in textRects.map({$0.cgRectValue}) {
        let underlineHeight: CGFloat = 2
        let newRect = CGRect(x: rect.origin.x, y: rect.origin.y + rect.height - (underlineHeight/2), 
                             width: rect.width, height: underlineHeight)
        paths.append(UIBezierPath(rect: newRect))
    }
                
    completion(paths)

}
```

In addition to providing the proofreading mark shapes, Writing Tools also asks you to provide the bounding rectangles for the text itself. Writing Tools uses these bounding rectangles to draw highlights around your text. The following example retrieves the bounding rectangles for the specified range of text and passes a Bézier path for each rectangle to the completion handler:

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: UIWritingToolsCoordinator, 
        requestsBoundingBezierPathsFor range: NSRange, 
        in context: UIWritingToolsCoordinator.Context, 
        completion: @escaping ([UIBezierPath]) -> Void) {

    let textRects = getTextRectangles(range)   // Returns an array of NSValue<NSRect*>.
        
    var paths = [UIBezierPath]()
    for rect in textRects.map({$0.cgRectValue}) {
        paths.append(UIBezierPath(rect: rect))
    }
                
    completion(paths)
}
```

##### Respond to State Changes

During the course of changing content, the state of the Writing Tools system changes based on what’s happening. Writing Tools starts in the inactive state, but quickly moves to other states based on the type of experience it creates. When a person accepts or rejects the changes for the current operation, Writing Tools moves back to inactive state. You might use your delegate’s [`writingToolsCoordinator(_:willChangeTo:completion:)`](uiwritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:).md) method to respond to the following types of changes:

- Use a transition to the [`UIWritingToolsCoordinator.State.inactive`](uiwritingtoolscoordinator/state-swift.enum/inactive.md) state to clear any cached data from the previous operation.
- Use transitions to the [`UIWritingToolsCoordinator.State.noninteractive`](uiwritingtoolscoordinator/state-swift.enum/noninteractive.md) or [`UIWritingToolsCoordinator.State.interactiveResting`](uiwritingtoolscoordinator/state-swift.enum/interactiveresting.md) state to determine the level of interactivity with your view.
- Use a transition to the [`UIWritingToolsCoordinator.State.interactiveStreaming`](uiwritingtoolscoordinator/state-swift.enum/interactivestreaming.md) state to start progress controls or otherwise indicate that Writing Tools is working on the request. In addition, use transitions to and from this state to implement undo coalescing. Specifically, start a new undo group on a transition to this state, and end that undo group on a transition away from this state. Notify Writing Tools of any undo stack changes by calling the [`updateRange(_:with:reason:forContextWithIdentifier:)`](uiwritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md) method.

For more information about how to handle individual states, see the [`UIWritingToolsCoordinator.State`](uiwritingtoolscoordinator/state-swift.enum.md) type.

##### Inform the Coordinator of External Changes to Your Content

When Writing Tools is active, it tracks changes to the text in your view. If you make changes to your view’s text storage while Writing Tools is active, let the system know immediately. Writing Tools tracks the changes it makes internally, so it needs to know about any external changes to make sure it delivers accurate information to your delegate object. To notify Writing Tools of any changes, use one of the following methods:

- Call the [`updateRange(_:with:reason:forContextWithIdentifier:)`](uiwritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md) method if you change the text that corresponds to text in one of your context objects. Depending on the scope of your changes, Writing Tools might incorporate your changes or abort the current operation altogether.
- Call the [`updateForReflowedTextInContextWithIdentifier(_:)`](uiwritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:).md) method to report any changes that affect your view’s layout. For example, call this method if the size of your view changes, or if you change the text that precedes what’s in one of your context objects. When you call this method, Writing Tools requests new previews, proofreading marks, and other layout-dependent information.

## See Also

- [class UIWritingToolsCoordinator](uiwritingtoolscoordinator.md)
  An object that manages interactions between Writing Tools and your custom text view.
- [UIWritingToolsCoordinator.Delegate](uiwritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
- [UIWritingToolsCoordinator.Context](uiwritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.
- [UIWritingToolsCoordinator.AnimationParameters](uiwritingtoolscoordinator/animationparameters.md)
  An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adding-writing-tools-support-to-a-custom-uiview)*