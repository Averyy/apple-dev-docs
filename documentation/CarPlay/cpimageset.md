# CPImageSet

**Framework**: CarPlay  
**Kind**: class

Light and dark representations of an image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPImageSet
```

#### Overview

CarPlay is set to dark appearance by default in most vehicles, but does provide the option to automatically switch between dark and light appearance. Use an image set to provide images for both appearances, and CarPlay displays the correct one for the current appearance.

## Topics

### Creating an Image Set
- [init(lightContentImage: UIImage, darkContentImage: UIImage)](cpimageset/init(lightcontentimage:darkcontentimage:).md)
  Creates an image set with light and dark versions of an image.
### Getting Content Images
- [var lightContentImage: UIImage](cpimageset/lightcontentimage.md)
  The image the system displays when the user interface style is light.
- [var darkContentImage: UIImage](cpimageset/darkcontentimage.md)
  The image the system displays when the user interface style is dark.
### Initializers
- [init?(coder: NSCoder)](cpimageset/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CPButton](cpbutton.md)
  A button that displays an image and invokes a handler when the user taps it.
- [let CarPlayErrorDomain: String](carplayerrordomain.md)
  The domain that CarPlay uses for any errors it provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageset)*