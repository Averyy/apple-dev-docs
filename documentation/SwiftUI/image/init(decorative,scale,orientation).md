# init(decorative:scale:orientation:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an unlabeled, decorative image based on a Core Graphics image instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(decorative cgImage: CGImage, scale: CGFloat, orientation: Image.Orientation = .up)
```

## Discussion

SwiftUI ignores this image for accessibility purposes.

## Parameters

- `cgImage`: The base graphical image.
- `scale`: The scale factor for the image, with a value like `1.0`, `2.0`, or `3.0`.
- `orientation`: The orientation of the image. The default is [`Image.Orientation.up`](./orientation/up.md).

## See Also

### Creating an image for decorative use
- [init(decorative: String, bundle: Bundle?)](./init%28decorative,bundle%29.md)
  Creates an unlabeled, decorative image.
- [init(decorative: String, variableValue: Double?, bundle: Bundle?)](./init%28decorative,variablevalue,bundle%29.md)
  Creates an unlabeled, decorative image, with a variable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(decorative:scale:orientation:))*