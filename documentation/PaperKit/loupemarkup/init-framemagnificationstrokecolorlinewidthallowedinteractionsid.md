# init(frame:magnification:strokeColor:lineWidth:allowedInteractions:id:)

**Framework**: PaperKit  
**Kind**: init

Initializes and returns a new loupe markup from the specified parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(frame: CGRect, magnification: CGFloat = 1.5, strokeColor: CGColor? = nil, lineWidth: CGFloat = 2.0, allowedInteractions: MarkupInteractions = .all, id: MarkupID<LoupeMarkup> = MarkupID())
```

## Parameters

- `frame`: The frame of the shape.
- `magnification`: The magnification level used to zoom the content below the loupe. Defaults to `1.5`.
- `strokeColor`: The color of the loupe’s border. Defaults to `nil` for no border.
- `lineWidth`: The width of the loupe’s border in points. Defaults to `2.0`.
- `allowedInteractions`: The flags controlling the interactions people can perform. Defaults to `.all`.
- `id`: The identity of the loupe. Defaults to a unique id.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/loupemarkup/init(frame:magnification:strokecolor:linewidth:allowedinteractions:id:))*