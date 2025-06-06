# CLKFullColorImageProvider

**Framework**: ClockKit  
**Kind**: class

A full-color image displayed by a complication.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKFullColorImageProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

All graphic complications support full-color images; however, some watch faces display these images as tinted images. Tinted images are black and white images with a highlight color that matches the watch face. If you don’t provide a tinted image provider, ClockKit automatically desaturates the full-color image to create the tinted image.

The template also often masks these image to produce circular images or rounded rectangles.

For information about the image sizes and masks, see [`Apple Watch Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/watch/human-interface-guidelines/).

## Topics

### Creating an Image Provider
- [convenience init(fullColorImage: UIImage)](clkfullcolorimageprovider/init(fullcolorimage:).md)
  Creates an image provider with the specified full-color image.
- [convenience init(fullColorImage: UIImage, tintedImageProvider: CLKImageProvider?)](clkfullcolorimageprovider/init(fullcolorimage:tintedimageprovider:).md)
  Creates an image provider that produces full-color and tinted images.
### Getting the Image Data
- [var image: UIImage](clkfullcolorimageprovider/image.md)
  The full-color image to display.
- [var tintedImageProvider: CLKImageProvider?](clkfullcolorimageprovider/tintedimageprovider.md)
  An image provider that produces alternative images for tinted graphic complications.
### Setting the Accessibility Label
- [var accessibilityLabel: String?](clkfullcolorimageprovider/accessibilitylabel.md)
  A succinct label that identifies the purpose of the image.
### Creating Empty Image Providers
- [init()](clkfullcolorimageprovider/init.md)
  Creates an empty full color image provider.
- [class func new() -> Self](clkfullcolorimageprovider/new.md)
  Creates an empty full color image provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKImageProvider](clkimageprovider.md)
  An image displayed by a complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider)*