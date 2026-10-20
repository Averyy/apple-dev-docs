# ColorSyncMD5

**Framework**: ColorSync  
**Kind**: struct  
**Role**: Structure

An MD5 digest that uniquely identifies a profile, as defined by the ICC specification.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ColorSyncMD5
```

```c
typedef struct { ... } ColorSyncMD5;
```

## Topics

### Initializers
- [init()](./colorsyncmd5/init%28%29.md)
- [init(digest: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))](./colorsyncmd5/init%28digest%29.md)
### Instance Properties
- [var digest: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./colorsyncmd5/digest.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Computing profile digests
- [func ColorSyncProfileGetMD5(ColorSyncProfile!) -> ColorSyncMD5](./colorsyncprofilegetmd5%28_%29.md)
  Returns the MD5 digest for a profile.
- [var COLORSYNC_MD5_LENGTH: Int32](./colorsync_md5_length.md)
- [var kColorSyncProfileMD5Digest: Unmanaged<CFString>!](./kcolorsyncprofilemd5digest.md)
  A key for the profile’s MD5 digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncmd5)*