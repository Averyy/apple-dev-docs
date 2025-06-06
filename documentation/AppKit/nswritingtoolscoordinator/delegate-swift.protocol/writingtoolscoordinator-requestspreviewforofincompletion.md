# writingToolsCoordinator(_:requestsPreviewFor:of:in:completion:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the delegate for a preview image and layout information for the specified text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, previewFor textAnimation: NSWritingToolsCoordinator.TextAnimation, range: NSRange, context: NSWritingToolsCoordinator.Context) async -> [NSTextPreview]?
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

During an interactive evaluation of your view’s text, Writing Tools creates different animations to provide feedback on what’s happening. As part of the preparation for those animations, Writing Tools asks you to provide a preview of the affected content in your view. Writing Tools uses this preview to build and execute the animations in the view stored in the [`effectContainerView`](nswritingtoolscoordinator/effectcontainerview.md) property of the coordinator object.

To build a preview of your content in macOS, render the specified range of text into an image with a transparent background and use that image to create your [`NSTextPreview`](nstextpreview.md) object directly. Set the [`presentationFrame`](nstextpreview/presentationframe.md) property to the rectangle in your view’s coordinate space that contains the text you captured. Set the [`candidateRects`](nstextpreview/candidaterects.md) property to the selection rectangles for the text, which you get from your view’s layout manager. Writing Tools uses this information to place your image directly above the text in your view.

For a single animation type, the system calls the `writingToolsCoordinator(_:prepareFor:range:context:completion:)` method, followed sequentially by this method and then the [`writingToolsCoordinator(_:finish:for:in:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md) method. Each method executes asynchronously, but the system calls the next method in the sequence only after you call the completion handler of the previous method. However, multiple animations can run simultaneously, so check the `textAnimation` parameter to differentiate sequences.

## Parameters

- `writingToolsCoordinator`: The coordinator object notifying you that   animations are about to begin.
- `textAnimation`: The type of animation Writing Tools is preparing.
- `range`: The range of text that requires a preview image. This range   is relative to the text in your context object, and it’s your responsibility   to match that location to the correct location in your text storage.   If you initialized the context object with the entire contents of   your view’s text storage, you can use   as-is to access that   text storage. However, if you initialized the context object with only   a portion of your view’s text, add the starting location of your   context object’s text to this value to get the correct range for that   text storage.
- `context`: The context object that contains the original text. Use this   object to fetch the current text, and to match that text to your   underlying text storage.
- `completion`: A completion handler to execute when you are done. The   handler has no return value and takes an   object   as a parameter. You must call this handler at some point during your implementation.

## See Also

- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSRect, in: NSWritingToolsCoordinator.Context, completion: (NSTextPreview?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, prepareFor: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:).md)
  Prepare for animations for the content that Writing Tools is evaluating.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, finish: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:))*