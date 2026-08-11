# init(shape:frame:rotation:fillColor:strokeColor:lineWidth:opacity:startLineMarker:endLineMarker:attributedText:allowedInteractions:autoresizing:id:)

**Framework**: PaperKit  
**Kind**: init

Initializes and returns a new shape markup from the specified parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(shape: ShapeMarkup.Shape, frame: CGRect, rotation: CGFloat = 0.0, fillColor: CGColor? = nil, strokeColor: CGColor? = nil, lineWidth: CGFloat = 1.0, opacity: CGFloat = 1.0, startLineMarker: ShapeMarkup.LineMarker = .none, endLineMarker: ShapeMarkup.LineMarker = .none, attributedText: AttributedString = Foundation.AttributedString(), allowedInteractions: MarkupInteractions = .all, autoresizing: MarkupAutoresizing = [], id: MarkupID<ShapeMarkup> = MarkupID())
```

## Parameters

- `shape`: The shape to create.
- `frame`: The frame of the shape.
- `rotation`: The rotation in radians of the shape. Defaults to `0.0` (no rotation).
- `fillColor`: The fill color of the shape. Defaults to `nil` (no fill).
- `strokeColor`: The stroke color of the shape’s outline. Defaults to `nil` (no stroke).
- `lineWidth`: The width of the shape’s stroke. Defaults to `1.0`.
- `opacity`: The opacity of the shape, ranging from `0.0` (fully transparent) to `1.0` (fully opaque). Defaults to `1.0`.
- `startLineMarker`: The marker style for the start of the line. Defaults to `.none`. Only applicable for open shape paths.
- `endLineMarker`: The marker style for the end of the line. Defaults to `.none`. Only applicable for open shape paths.
- `attributedText`: The attributed text displayed inside this shape. Defaults to the empty string.
- `allowedInteractions`: The flags controlling the interactions users can perform. Defaults to `.all`.
- `autoresizing`: The flags controlling autoresize behavior. Defaults to `[]`.
- `id`: The identity of the shape. Defaults to a unique id.

## See Also

- [init(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat)](shapemarkup/init(configuration:frame:rotation:).md)
  Initializes and returns a new shape markup from the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/shapemarkup/init(shape:frame:rotation:fillcolor:strokecolor:linewidth:opacity:startlinemarker:endlinemarker:attributedtext:allowedinteractions:autoresizing:id:))*