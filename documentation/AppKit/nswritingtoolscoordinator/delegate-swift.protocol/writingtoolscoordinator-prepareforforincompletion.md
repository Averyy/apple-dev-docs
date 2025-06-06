# writingToolsCoordinator(_:prepareFor:for:in:completion:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Prepare for animations for the content that Writing Tools is evaluating.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, prepareFor textAnimation: NSWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: NSWritingToolsCoordinator.Context) async
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

During an interactive evaluation of your view’s text, Writing Tools creates different animations to provide feedback on what’s happening. For example, it creates an [`NSWritingToolsCoordinator.TextAnimation.anticipate`](nswritingtoolscoordinator/textanimation/anticipate.md) animation to let people know the system is evaluating the text. The `textAnimation` parameter tells you what type of animation to prepare for.

Use this method to prepare for the system-provided animations of your view’s content. For interactive animations, hide the text in the specified range temporarily while the system animations run. For non-interactive animations, dim the text for the duration of the animation to indicate it’s not editable. For animations to remove or insert text, you can also use this method to set up animations to reflow your view’s content to match the changes. At the end of a given animation, use your delegate’s [`writingToolsCoordinator(_:finish:for:in:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md) method to undo any changes you make to your content.

For a single animation type, the system calls this method, followed sequentially by the `writingToolsCoordinator(_:previewFor:range:context:completion:)` and [`writingToolsCoordinator(_:finish:for:in:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md) methods. Each method executes asynchronously, but the system calls the next method in the sequence only after you call the completion handler of the previous method. However, multiple animations can run simultaneously, so check the `textAnimation` and `range` parameters to differentiate sequences.

## Parameters

- `writingToolsCoordinator`: The coordinator object notifying you that   animations are about to begin.
- `textAnimation`: The type of animation Writing Tools is preparing.
- `range`: The range of text affected by the animation. This range is   relative to the text in your context object, and it’s your responsibility   to match that location to the correct location in your text storage.   If you initialized the context object with the entire contents of your   view’s text storage, you can use   as-is to access that text   storage. However, if you initialized the context object with only a portion   of your view’s text, add the starting location of your context object’s   text to this value to get the correct range for that text storage.
- `context`: The context object that contains the original text. Use this   object to fetch the current text, and to match that text to your underlying   text storage.
- `completion`: A completion handler to execute when you are done. The handler   has no return value and takes no parameters. You must call this handler   at some point during your implementation.

## See Also

- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSWritingToolsCoordinator.TextAnimation, of: NSRange, in: NSWritingToolsCoordinator.Context, completion: ([NSTextPreview]?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSRect, in: NSWritingToolsCoordinator.Context, completion: (NSTextPreview?) -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:in:completion:).md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, finish: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:finish:for:in:completion:).md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:preparefor:for:in:completion:))*