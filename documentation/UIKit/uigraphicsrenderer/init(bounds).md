# init(bounds:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithBounds:(CGRect) bounds;
```

## Return Value

An initialized graphics renderer.

## Discussion

Use this initializer to create a graphics renderer that operates on Core Graphics contexts with the specified bounds. This initializer uses the [`default()`](../uigraphicsrendererformat/default%28%29.md) static method on [`UIGraphicsRendererFormat`](../uigraphicsrendererformat.md) to create the renderer’s format, thereby selecting parameters that are the most appropriate for the current device.

## Parameters

- `bounds`: The bounds of the Core Graphics context available to the renderer, with values measured in points.

## See Also

### Initializing a graphics renderer
- [init(bounds: CGRect, format: UIGraphicsRendererFormat)](./init%28bounds,format%29.md)
  Creates a new graphics renderer with the given bounds and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderer/init(bounds:))*