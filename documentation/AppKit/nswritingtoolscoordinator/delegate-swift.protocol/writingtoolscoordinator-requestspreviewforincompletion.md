# writingToolsCoordinator(_:requestsPreviewFor:in:completion:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Asks the delegate for a preview image and layout information for the specified text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, previewFor rect: NSRect, context: NSWritingToolsCoordinator.Context) async -> NSTextPreview?
```

#### Discussion

During an interactive evaluation of your view’s text, Writing Tools creates different animations to provide feedback on what’s happening. As part of the preparation for those animations, Writing Tools asks you to provide a preview of the affected content in your view. Writing Tools uses this preview to build and execute the animations in the view stored in the [`effectContainerView`](nswritingtoolscoordinator/effectcontainerview.md) property of the coordinator object.

To build a preview of your content in macOS, render the requested portion of your view into an image with a transparent background and use that image to create your [`NSTextPreview`](nstextpreview.md) object directly. Set the [`presentationFrame`](nstextpreview/presentationframe.md) property to the specified rectangle. Set the [`candidateRects`](nstextpreview/candidaterects.md) property to the selection rectangles for the associated text, which you get from your view’s layout manager. Writing Tools uses this information to place your image directly above the text in your view.

For a single animation type, the system calls the `writingToolsCoordinator(_:prepareFor:range:context:completion:)` method, followed sequentially by this method and then the [`writingToolsCoordinator(_:finish:for:in:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md) method. Each method executes asynchronously, but the system calls the next method in the sequence only after you call the completion handler of the previous method. However, multiple animations can run simultaneously, so check the `textAnimation` parameter to differentiate sequences.

## Parameters

- `writingToolsCoordinator`: The coordinator object notifying you that   animations are about to begin.
- `rect`: The portion of your view that contains the requested text. This rectangle is in the view’s coordinate system.
- `context`: The context object that contains the original text. Use this   object to fetch the current text, and to match that text to your   underlying text storage.
- `completion`: A completion handler to execute when you are done. The   handler has no return value and takes an   object   as a parameter. You must call this handler at some point during your implementation.

## See Also

- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSWritingToolsCoordinator.TextAnimation, of: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSTextPreview]?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, prepareFor: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:).md)
  Prepare for animations for the content that Writing Tools is evaluating.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, finish: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:in:completion:))*