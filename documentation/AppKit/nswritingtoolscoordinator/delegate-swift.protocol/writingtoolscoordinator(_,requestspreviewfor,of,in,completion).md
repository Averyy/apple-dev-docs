# writingToolsCoordinator(_:requestsPreviewFor:of:in:completion:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate for a preview image and layout information for the specified text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, requestsPreviewFor textAnimation: NSWritingToolsCoordinator.TextAnimation, of range: NSRange, in context: NSWritingToolsCoordinator.Context, completion: @escaping @Sendable ([NSTextPreview]?) -> Void)
```

```swift
func writingToolsCoordinator(_ writingToolsCoordinator: NSWritingToolsCoordinator, previewFor textAnimation: NSWritingToolsCoordinator.TextAnimation, range: NSRange, context: NSWritingToolsCoordinator.Context) async -> [NSTextPreview]?
```

```objc
- (void) writingToolsCoordinator:(NSWritingToolsCoordinator *) writingToolsCoordinator requestsPreviewForTextAnimation:(NSWritingToolsCoordinatorTextAnimation) textAnimation ofRange:(NSRange) range inContext:(NSWritingToolsCoordinatorContext *) context completion:(void (^)(NSArray<NSTextPreview *> *textPreviews)) completion;
```

## Mentions

- [Adding Writing Tools support to a custom AppKit view](../../adding-writing-tools-support-to-a-custom-nsview.md)

#### Discussion

During an interactive evaluation of your view’s text, Writing Tools creates different animations to provide feedback on what’s happening. As part of the preparation for those animations, Writing Tools asks you to provide a preview of the affected content in your view. Writing Tools uses this preview to build and execute the animations in the view stored in the [`effectContainerView`](../effectcontainerview.md) property of the coordinator object.

To build a preview of your content in macOS, render the specified range of text into an image with a transparent background and use that image to create your [`NSTextPreview`](../../nstextpreview.md) object directly. Set the [`presentationFrame`](../../nstextpreview/presentationframe.md) property to the rectangle in your view’s coordinate space that contains the text you captured. Set the [`candidateRects`](../../nstextpreview/candidaterects.md) property to an array containing one rectangle per line of the selected text, which you get from your view’s layout manager.

> ❗ **Important**: Provide one rectangle per line in `candidateRects`. Writing Tools uses each rectangle to animate its line independently, producing a bounce effect. If you provide a single rectangle that spans the entire range instead, Writing Tools can only animate the text as one unit, which produces a shimmer instead of a bounce.

For a single animation type, the system calls the [`writingToolsCoordinator(_:prepareFor:for:in:completion:)`](./writingtoolscoordinator%28_,preparefor,for,in,completion%29.md) method, followed sequentially by this method and then the [`writingToolsCoordinator(_:finish:for:in:completion:)`](./writingtoolscoordinator%28_,finish,for,in,completion%29.md) method. Each method executes asynchronously, but the system calls the next method in the sequence only after you call the completion handler of the previous method. However, multiple animations can run simultaneously, so check the `textAnimation` parameter to differentiate sequences.

## Parameters

- `writingToolsCoordinator`: The coordinator object notifying you that animations are about to begin.
- `textAnimation`: The type of animation Writing Tools is preparing.
- `range`: The range of text that requires a preview image. This range is relative to the text in your context object, and it’s your responsibility to match that location to the correct location in your text storage. If you initialized the context object with the entire contents of your view’s text storage, you can use `range` as-is to access that text storage. However, if you initialized the context object with only a portion of your view’s text, add the starting location of your context object’s text to this value to get the correct range for that text storage.
- `context`: The context object that contains the original text. Use this object to fetch the current text, and to match that text to your underlying text storage.
- `completion`: A completion handler to execute when you are done. The handler has no return value and takes an [`NSTextPreview`](../../nstextpreview.md) object as a parameter. You must call this handler at some point during your implementation.

## See Also

### Animating inline text changes
- [func writingToolsCoordinator(NSWritingToolsCoordinator, requestsPreviewFor: NSRect, in: NSWritingToolsCoordinator.Context, completion: (NSTextPreview?) -> Void)](./writingtoolscoordinator%28_,requestspreviewfor,in,completion%29.md)
  Asks the delegate for a preview image and layout information for the specified text.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, prepareFor: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](./writingtoolscoordinator%28_,preparefor,for,in,completion%29.md)
  Prepare for animations for the content that Writing Tools is evaluating.
- [func writingToolsCoordinator(NSWritingToolsCoordinator, finish: NSWritingToolsCoordinator.TextAnimation, for: NSRange, in: NSWritingToolsCoordinator.Context, completion: () -> Void)](./writingtoolscoordinator%28_,finish,for,in,completion%29.md)
  Asks the delegate to clean up any state related to the specified Writing Tools animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:completion:))*