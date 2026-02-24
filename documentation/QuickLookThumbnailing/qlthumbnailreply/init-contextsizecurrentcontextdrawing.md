# init(contextSize:currentContextDrawing:)

**Framework**: Quick Look Thumbnailing  
**Kind**: init

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

#### Return Value

An initialized reply object for a requested thumbnail.

#### Discussion

Use this initializer if you’re drawing the thumbnail using [`UIKit`](https://developer.apple.com/documentation/UIKit) or [`AppKit`](https://developer.apple.com/documentation/AppKit). If you’re using CoreGraphics to draw the thumbnail, use [`init(contextSize:drawing:)`](qlthumbnailreply/init(contextsize:drawing:).md). The context that this initializer provides uses the coordinate system of [`UIKit`](https://developer.apple.com/documentation/UIKit) or [`AppKit`](https://developer.apple.com/documentation/AppKit), depending on the platform.

## Parameters

- `contextSize`: The desired size of the context that you pass to the drawing block. Set this value as close as possible to the [`QLFileThumbnailRequest`](qlfilethumbnailrequest.md) class’s [`maximumSize`](qlfilethumbnailrequest/maximumsize.md) value and greater than or equal to its [`minimumSize`](qlfilethumbnailrequest/minimumsize.md) value. This parameter indicates the preferred size of the thumbnail. The context’s width or its height matches the `width` or `height` of the [`maximumSize`](qlfilethumbnailrequest/maximumsize.md), or, ideally, both. The system scales the context size to the [`QLFileThumbnailRequest`](qlfilethumbnailrequest.md) class’s [`scale`](qlfilethumbnailrequest/scale.md) property. For example, if you pass a `contextSize` of `CGSize(10, 10)` to this method, the size of the context is `(scale * 10, scale * 10)`.
- `drawingBlock`: A block that draws the thumbnail into the current bitmap [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) that’s accessible using [`UIGraphicsGetCurrentContext()`](https://developer.apple.com/documentation/UIKit/UIGraphicsGetCurrentContext()) or, if you’re developing for macOS, `NSGraphicsContext.current`. Use the context with the coordinate system of [`UIKit`](https://developer.apple.com/documentation/UIKit) or [`AppKit`](https://developer.apple.com/documentation/AppKit). Return [`true`](https://developer.apple.com/documentation/Swift/true) if you successfully drew the thumbnail into the context. Return [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [convenience init(contextSize: CGSize, drawing: (CGContext) -> Bool)](qlthumbnailreply/init(contextsize:drawing:).md)
  Creates a new thumbnail for a custom file type in the given context.
- [convenience init(imageFileURL: URL)](qlthumbnailreply/init(imagefileurl:).md)
  Creates a new thumbnail for a custom file type using a file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply/init(contextsize:currentcontextdrawing:))*