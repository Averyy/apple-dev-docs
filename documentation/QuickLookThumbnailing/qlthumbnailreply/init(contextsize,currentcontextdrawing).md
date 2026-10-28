# init(contextSize:currentContextDrawing:)

**Framework**: Quick Look Thumbnailing  
**Kind**: init  
**Role**: Initializer

Creates a new thumbnail for a custom file type in the current context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(contextSize: CGSize, currentContextDrawing drawingBlock: @escaping () -> Bool)
```

```objc
+ (instancetype) replyWithContextSize:(CGSize) contextSize currentContextDrawingBlock:(BOOL (^)()) drawingBlock;
```

## Return Value

An initialized reply object for a requested thumbnail.

## Discussion

Use this initializer if you’re drawing the thumbnail using [UIKit](../../UIKit/UIKit.md) or [AppKit](../../AppKit/AppKit.md). If you’re using CoreGraphics to draw the thumbnail, use [`init(contextSize:drawing:)`](./init%28contextsize,drawing%29.md). The context that this initializer provides uses the coordinate system of [UIKit](../../UIKit/UIKit.md) or [AppKit](../../AppKit/AppKit.md), depending on the platform.

## Parameters

- `contextSize`: The desired size of the context that you pass to the drawing block. Set this value as close as possible to the [`QLFileThumbnailRequest`](../qlfilethumbnailrequest.md) class’s [`maximumSize`](../qlfilethumbnailrequest/maximumsize.md) value and greater than or equal to its [`minimumSize`](../qlfilethumbnailrequest/minimumsize.md) value.

  This parameter indicates the preferred size of the thumbnail. The context’s width or its height matches the `width` or `height` of the [`maximumSize`](../qlfilethumbnailrequest/maximumsize.md), or, ideally, both.

  The system scales the context size to the [`QLFileThumbnailRequest`](../qlfilethumbnailrequest.md) class’s [`scale`](../qlfilethumbnailrequest/scale.md) property. For example, if you pass a `contextSize` of `CGSize(10, 10)` to this method, the size of the context is `(scale * 10, scale * 10)`.
- `drawingBlock`: A block that draws the thumbnail into the current bitmap [`CGContext`](../../CoreGraphics/cgcontext.md) that’s accessible using [`UIGraphicsGetCurrentContext()`](../../UIKit/uigraphicsgetcurrentcontext%28%29.md) or, if you’re developing for macOS, `NSGraphicsContext.current`. Use the context with the coordinate system of [UIKit](../../UIKit/UIKit.md) or [AppKit](../../AppKit/AppKit.md).

  Return [`true`](../../Swift/true.md) if you successfully drew the thumbnail into the context. Return [`false`](../../Swift/false.md) otherwise.

## See Also

### Creating a Thumbnail
- [convenience init(contextSize: CGSize, drawing: (CGContext) -> Bool)](./init%28contextsize,drawing%29.md)
  Creates a new thumbnail for a custom file type in the given context.
- [convenience init(imageFileURL: URL)](./init%28imagefileurl%29.md)
  Creates a new thumbnail for a custom file type using a file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply/init(contextsize:currentcontextdrawing:))*