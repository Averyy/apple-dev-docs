# init(bounds:)

**Framework**: UIKit  
**Kind**: init

Creates a new graphics renderer with the specified bounds and a default format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(bounds: CGRect)
```

#### Return Value

An initialized graphics renderer.

#### Discussion

Use this initializer to create a graphics renderer that operates on Core Graphics contexts with the specified bounds. This initializer uses the [`default()`](uigraphicsrendererformat/default().md) static method on [`UIGraphicsRendererFormat`](uigraphicsrendererformat.md) to create the renderer’s format, thereby selecting parameters that are the most appropriate for the current device.

## Parameters

- `bounds`: The bounds of the Core Graphics context available to the renderer, with values measured in points.

## See Also

- [init(bounds: CGRect, format: UIGraphicsRendererFormat)](uigraphicsrenderer/init(bounds:format:).md)
  Creates a new graphics renderer with the given bounds and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/init(bounds:))*