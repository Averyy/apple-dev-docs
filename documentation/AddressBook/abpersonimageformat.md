# ABPersonImageFormat

**Framework**: Address Book  
**Kind**: struct

Indicates an image format.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct ABPersonImageFormat
```

#### Overview

See `Image Format`.

## Topics

### Constants
- [init(UInt32)](abpersonimageformat/init(_:).md)
  Initializes an image format with an integer value.
- [init(rawValue: UInt32)](abpersonimageformat/init(rawvalue:).md)
  Initializes an image format with a raw integer value.
### Instance Properties
- [var rawValue: UInt32](abpersonimageformat/rawvalue.md)
  The raw value of an image format.
- [var kABPersonImageFormatOriginalSize: ABPersonImageFormat](kabpersonimageformatoriginalsize.md)
  The image at its original size and shape.
- [var kABPersonImageFormatThumbnail: ABPersonImageFormat](kabpersonimageformatthumbnail.md)
  The small square thumbnail.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum ABAuthorizationStatus](abauthorizationstatus.md)
  Different possible values for the authorization status of an app with respect to address book data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonimageformat)*