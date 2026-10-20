# UIDisplayGamut

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the gamut of the current display.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UIDisplayGamut
```

```c
enum UIDisplayGamut : NSInteger;
```

## Topics

### Constants
- [UIDisplayGamut.unspecified](./uidisplaygamut/unspecified.md)
  An unspecified gamut value.
- [UIDisplayGamut.SRGB](./uidisplaygamut/srgb.md)
  The sRGB display gamut.
- [UIDisplayGamut.P3](./uidisplaygamut/p3.md)
  The P3 display gamut.
### Initializers
- [init?(rawValue: Int)](./uidisplaygamut/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Retrieving display-related traits
- [var displayScale: CGFloat](./uitraitcollection/displayscale.md)
  The display scale of the trait collection.
- [var displayGamut: UIDisplayGamut](./uitraitcollection/displaygamut.md)
  The gamut of the current display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidisplaygamut)*