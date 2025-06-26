# blackBlock

**Framework**: Core Video  
**Kind**: property

The bit pattern for a block of black pixels.  If absent, black is assumed to be all zeros. Otherwise, this should be [`bitsPerBlock`](cvpixelformatdescription/pixellayout/bitsperblock.md) bits long. If bitsPerBlock is less than a byte, repeat the bit pattern for the full byte.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var blackBlock: Data?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/pixellayout/blackblock)*