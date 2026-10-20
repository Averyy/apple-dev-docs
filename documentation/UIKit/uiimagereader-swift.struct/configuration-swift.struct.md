# UIImageReader.Configuration

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The properties that a reader uses to decode images.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating the configuration
- [init()](./configuration-swift.struct/init%28%29.md)
  Creates a new instance of the image reader configuration.
### Configuration properties
- [var prefersHighDynamicRange: Bool](./configuration-swift.struct/prefershighdynamicrange.md)
  A Boolean value that indicates whether the image reader should decode the image as HDR when the type is capable of decoding in either SDR or HDR.
- [var preparesImagesForDisplay: Bool](./configuration-swift.struct/preparesimagesfordisplay.md)
  A Boolean value that indicates whether the image reader prepares the image for display.
- [var preferredThumbnailSize: CGSize](./configuration-swift.struct/preferredthumbnailsize.md)
  The thumbnail size in pixels that the image reader makes the image.
- [var pixelsPerInch: Double](./configuration-swift.struct/pixelsperinch.md)
  The integral scale that the image reader applies to the image.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagereader-swift.struct/configuration-swift.struct)*