# Gradient.ColorSpace

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A method of interpolating between the colors in a gradient.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ColorSpace
```

## Topics

### Getting an interpolation method
- [static let device: Gradient.ColorSpace](./colorspace/device.md)
  Interpolates gradient colors in the output color space.
- [static let perceptual: Gradient.ColorSpace](./colorspace/perceptual.md)
  Interpolates gradient colors in a perceptual color space.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with color spaces
- [func colorSpace(Gradient.ColorSpace) -> AnyGradient](./colorspace%28_%29.md)
  Returns a version of the gradient that will use a specified color space for interpolating between its colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gradient/colorspace)*