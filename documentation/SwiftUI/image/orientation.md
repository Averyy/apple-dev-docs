# Image.Orientation

**Framework**: SwiftUI  
**Kind**: enum

The orientation of an image.

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
@frozen
enum Orientation
```

#### Overview

Many image formats such as JPEG include orientation metadata in the image data. In other cases, you can specify image orientation in code. Properly specifying orientation is often important both for displaying the image and for certain kinds of image processing.

In SwiftUI, you provide an orientation value when initializing an [`Image`](image.md) from an existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage).

## Topics

### Getting image orientations
- [Image.Orientation.up](image/orientation/up.md)
  A value that indicates the original pixel data matches the image’s intended display orientation.
- [Image.Orientation.down](image/orientation/down.md)
  A value that indicates a 180° rotation of the image from the orientation of its original pixel data.
- [Image.Orientation.left](image/orientation/left.md)
  A value that indicates a 90° counterclockwise rotation from the orientation of its original pixel data.
- [Image.Orientation.right](image/orientation/right.md)
  A value that indicates a 90° clockwise rotation of the image from the orientation of its original pixel data.
### Getting mirrored image orientation
- [Image.Orientation.upMirrored](image/orientation/upmirrored.md)
  A value that indicates a horizontal flip of the image from the orientation of its original pixel data.
- [Image.Orientation.downMirrored](image/orientation/downmirrored.md)
  A value that indicates a vertical flip of the image from the orientation of its original pixel data.
- [Image.Orientation.leftMirrored](image/orientation/leftmirrored.md)
  A value that indicates a 90° clockwise rotation and horizontal flip of the image from the orientation of its original pixel data.
- [Image.Orientation.rightMirrored](image/orientation/rightmirrored.md)
  A value that indicates a 90° counterclockwise rotation and horizontal flip from the orientation of its original pixel data.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Fitting images into available space](fitting-images-into-available-space.md)
  Adjust the size and shape of images in your app’s user interface by applying view modifiers.
- [func imageScale(Image.Scale) -> some View](view/imagescale(_:).md)
  Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [var imageScale: Image.Scale](environmentvalues/imagescale.md)
  The image scale for this environment.
- [Image.Scale](image/scale.md)
  A scale to apply to vector images relative to text.
- [Image.ResizingMode](image/resizingmode.md)
  The modes that SwiftUI uses to resize an image to fit within its containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/orientation)*