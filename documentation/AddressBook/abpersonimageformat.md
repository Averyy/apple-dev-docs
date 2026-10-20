# ABPersonImageFormat

**Framework**: Address Book  
**Kind**: struct  
**Role**: Structure

Indicates an image format.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
struct ABPersonImageFormat
```

```c
typedef enum { ... } ABPersonImageFormat;
```

#### Overview

See `Image Format`.

## Topics

### Constants
- [init(UInt32)](./abpersonimageformat/init%28_%29.md)
  Initializes an image format with an integer value.
- [init(rawValue: UInt32)](./abpersonimageformat/init%28rawvalue%29.md)
  Initializes an image format with a raw integer value.
### Instance Properties
- [var rawValue: UInt32](./abpersonimageformat/rawvalue.md)
  The raw value of an image format.
- [var kABPersonImageFormatOriginalSize: ABPersonImageFormat](./kabpersonimageformatoriginalsize.md)
  The image at its original size and shape.
- [var kABPersonImageFormatThumbnail: ABPersonImageFormat](./kabpersonimageformatthumbnail.md)
  The small square thumbnail.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Deprecated
- [enum ABAuthorizationStatus](./abauthorizationstatus.md)
  Different possible values for the authorization status of an app with respect to address book data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonimageformat)*