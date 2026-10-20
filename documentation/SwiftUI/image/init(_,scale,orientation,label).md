# init(_:scale:orientation:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a labeled image based on a Core Graphics image instance, usable as content for controls.

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
init(_ cgImage: CGImage, scale: CGFloat, orientation: Image.Orientation = .up, label: Text)
```

## Parameters

- `cgImage`: The base graphical image.
- `scale`: The scale factor for the image, with a value like `1.0`, `2.0`, or `3.0`.
- `orientation`: The orientation of the image. The default is [`Image.Orientation.up`](./orientation/up.md).
- `label`: The label associated with the image. SwiftUI uses the label for accessibility.

## See Also

### Creating an image for use as a control
- [init(String, bundle: Bundle?, label: Text)](./init%28_,bundle,label%29.md)
  Creates a labeled image that you can use as content for controls, with the specified label.
- [init(String, variableValue: Double?, bundle: Bundle?, label: Text)](./init%28_,variablevalue,bundle,label%29.md)
  Creates a labeled image that you can use as content for controls, with the specified label and variable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(_:scale:orientation:label:))*