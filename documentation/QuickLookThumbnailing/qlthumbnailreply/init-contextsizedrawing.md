# init(contextSize:drawing:)

**Framework**: Quick Look Thumbnailing  
**Kind**: init

Creates a new thumbnail for a custom file type in the given context.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(contextSize: CGSize, drawing drawingBlock: @escaping (CGContext) -> Bool)
```

#### Return Value

An initialized reply object for a requested thumbnail.

#### Discussion

Use this initializer if you’re drawing the thumbnail using [`Core Graphics`](https://developer.apple.com/documentation/CoreGraphics). If you’re using [`UIKit`](https://developer.apple.com/documentation/UIKit) or [`AppKit`](https://developer.apple.com/documentation/AppKit) to draw the thumbnail, use the initializer [`init(contextSize:currentContextDrawing:)`](qlthumbnailreply/init(contextsize:currentcontextdrawing:).md). The context that this initializer provides uses the coordinate system of [`Core Graphics`](https://developer.apple.com/documentation/CoreGraphics).

## Parameters

- `contextSize`: The system scales the context size to the   class’s   property. For example, if you pass a   of   to this method, the size of the context is  .
- `drawingBlock`: Return   if you successfully drew the thumbnail into the context. Return   otherwise.

## See Also

- [convenience init(contextSize: CGSize, currentContextDrawing: () -> Bool)](qlthumbnailreply/init(contextsize:currentcontextdrawing:).md)
  Creates a new thumbnail for a custom file type in the current context.
- [convenience init(imageFileURL: URL)](qlthumbnailreply/init(imagefileurl:).md)
  Creates a new thumbnail for a custom file type using a file at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply/init(contextsize:drawing:))*