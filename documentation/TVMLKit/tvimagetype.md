# TVImageType

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

The type of image.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVImageType
```

```c
enum TVImageType : NSInteger;
```

## Topics

### Constants
- [TVImageType.image](./tvimagetype/image.md)
  The image is presented in its actual size.
- [TVImageType.fullscreen](./tvimagetype/fullscreen.md)
  The image occupies the entire screen.
- [TVImageType.decoration](./tvimagetype/decoration.md)
  The image is a decoration image, which is used to display an image inside of another image.
- [TVImageType.hero](./tvimagetype/hero.md)
  The image is a hero image, which is used to display a product image.
### Initializers
- [init?(rawValue: Int)](./tvimagetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Identifying an Image
- [var url: URL?](./tvimageelement/url.md)
  A URL that points to the location of the image.
- [var imageType: TVImageType](./tvimageelement/imagetype.md)
  The type of image.
- [var srcset: [String : URL]?](./tvimageelement/srcset.md)
  A dictionary specifying versions of the same image for different resolutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvimagetype)*