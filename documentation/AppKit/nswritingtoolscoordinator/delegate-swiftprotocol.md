# NSWritingToolsCoordinator.Delegate

**Framework**: AppKit  
**Kind**: protocol

An interface that you use to manage interactions between Writing Tools and your custom text view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
protocol Delegate : NSObjectProtocol
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Overview

Adopt the `NSWritingToolsCoordinator.Delegate` protocol in the type you use to manage your custom text view. When you add a [`NSWritingToolsCoordinator`](nswritingtoolscoordinator.md) object to your view, the coordinator uses this protocol to communicate with that view. The protocol lets Writing Tools fetch your view’s text, report suggested changes back to your view, and deliver visual feedback when Writing Tools features are active. Make sure the type that adopts this protocol has access to your view’s text storage and can perform relevant tasks on behalf of the view.

Writing Tools expects you to call the provided handler blocks at the end of your delegate methods. It’s crucial that you execute these blocks in a timely manner to allow Writing Tools to perform subsequent tasks. For example, Writing Tools waits for you to execute the handlers for animation-related methods before moving on to the next stage of the animations.

## Topics

### Starting a Writing Tools operation
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsContextsFor: NSWritingToolsCoordinator.ContextScope, completion: ([NSWritingToolsCoordinator.Context]) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestscontextsfor:completion:).md)
  Asks your delegate to provide the text to evaluate during the Writing Tools operation.
### Incorporating Writing Tools suggestions
- [func writingToolsCoordinator(NSWritingToolsCoordinator, replace: NSRange, in: NSWritingToolsCoordinator.Context, proposedText: NSAttributedString, reason: NSWritingToolsCoordinator.TextReplacementReason, animationParameters: NSWritingToolsCoordinator.AnimationParameters?, completion: (NSAttributedString?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:replace:in:proposedtext:reason:animationparameters:completion:).md)
  Tells the delegate that there are text changes to incorporate into the view.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, select: [NSValue], in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:select:in:completion:).md)
  Asks the delegate to update your view’s current text selection.
### Responding to lifecycle changes
- [func writingToolsCoordinator(NSWritingToolsCoordinator, willChangeTo: NSWritingToolsCoordinator.State, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:willchangeto:completion:).md)
  Notifies your delegate of relevant state changes when Writing Tools is running in your view.
### Animating inline text changes
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSWritingToolsCoordinator.TextAnimation, of: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSTextPreview]?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSRect, in: NSWritingToolsCoordinator.Context, completion: (NSTextPreview?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, prepareFor: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:).md)
  Prepare for animations for the content that Writing Tools is evaluating.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, finish: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.
### Displaying proofreading marks
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsRangeInContextWithIdentifierFor: NSPoint, completion: (NSRange, UUID) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsrangeincontextwithidentifierfor:completion:).md)
  Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsBoundingBezierPathsFor: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSBezierPath]) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsboundingbezierpathsfor:in:completion:).md)
  Asks the delegate to provide the bounding paths for the specified text in your view.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsUnderlinePathsFor: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSBezierPath]) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsunderlinepathsfor:in:completion:).md)
  Asks the delegate to provide an underline shape for the specified text during a proofreading session.
### Providing animation container views dynamically
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsSingleContainerSubrangesOf: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSValue]) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestssinglecontainersubrangesof:in:completion:).md)
  Asks the delegate to divide the specified range of text into the separate containers that render that text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsDecorationContainerViewFor: NSRange, in: NSWritingToolsCoordinator.Context, completion: (NSView) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestsdecorationcontainerviewfor:in:completion:).md)
  Asks the delegate to provide a decoration view for the specified range of text.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
  Adopt a simplified version of the Writing Tools experience in a custom view using the pasteboard and macOS services.
- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)
  Integrate Writing Tools support, including support for inline replacement animations, to your custom text views on macOS.
- [class NSWritingToolsCoordinator](nswritingtoolscoordinator.md)
  An object that manages interactions between Writing Tools and your custom text view.
- [NSWritingToolsCoordinator.Context](nswritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.
- [NSWritingToolsCoordinator.AnimationParameters](nswritingtoolscoordinator/animationparameters.md)
  An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.
- [Enhancing your custom text engine with Writing Tools](enhancing-your-custom-text-engine-with-writing-tools.md)
  Add Writing Tools support to your custom text engine to enhance the text editing experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol)*