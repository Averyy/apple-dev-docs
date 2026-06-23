# init(image:frame:rotation:opacity:contentsBounds:accessibilityDescription:allowedInteractions:id:)

**Framework**: PaperKit  
**Kind**: init

Initializes and returns a new image markup from the specified parameters.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(image: NSImage, frame: CGRect, rotation: CGFloat = 0.0, opacity: CGFloat = 1.0, contentsBounds: CGRect = CGRect(x: 0, y: 0, width: 1, height: 1), accessibilityDescription: String? = nil, allowedInteractions: MarkupInteractions = .all, id: MarkupID<ImageMarkup> = MarkupID())
```

#### Discussion

Image content is shown scaled to fill.

## Parameters

- `image`: The image content to display.
- `frame`: The frame of the image.
- `rotation`: The rotation in radians of the image. Defaults to `0.0` (no rotation).
- `opacity`: The opacity of the image, ranging from `0.0` (fully transparent) to `1.0` (fully opaque). Defaults to `1.0`.
- `contentsBounds`: The portion of the image to display, in normalized coordinates from `0.0` to `1.0`. Defaults to `CGRect(x: 0, y: 0, width: 1, height: 1)` (full image).
- `accessibilityDescription`: The accessibility description of the image for assistive technologies. Defaults to `nil`.
- `allowedInteractions`: The flags controlling the interactions users can perform. Defaults to `.all`.
- `id`: The identity of the image. Defaults to a unique id.

## See Also

- [init(image: CGImage, frame: CGRect, rotation: CGFloat, orientation: CGImagePropertyOrientation, opacity: CGFloat, contentsBounds: CGRect, accessibilityDescription: String?, allowedInteractions: MarkupInteractions, id: MarkupID<ImageMarkup>)](imagemarkup/init(image:frame:rotation:orientation:opacity:contentsbounds:accessibilitydescription:allowedinteractions:id:).md)
  Initializes and returns a new image markup from the specified parameters.
- [init?(image: UIImage, frame: CGRect, rotation: CGFloat, opacity: CGFloat, contentsBounds: CGRect, accessibilityDescription: String?, allowedInteractions: MarkupInteractions, id: MarkupID<ImageMarkup>)](imagemarkup/init(image:frame:rotation:opacity:contentsbounds:accessibilitydescription:allowedinteractions:id:)-8y6o9.md)
  Initializes and returns a new image markup from the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/init(image:frame:rotation:opacity:contentsbounds:accessibilitydescription:allowedinteractions:id:)-1ggjv)*