# srcset

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A dictionary specifying versions of the same image for different resolutions.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var srcset: [String : URL]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,NSURL *> * srcset;
```

#### Discussion

Each dictionary entry contains a string and a URL for a specific image.

## See Also

### Identifying an Image
- [var url: URL?](./url.md)
  A URL that points to the location of the image.
- [var imageType: TVImageType](./imagetype.md)
  The type of image.
- [enum TVImageType](../tvimagetype.md)
  The type of image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvimageelement/srcset)*