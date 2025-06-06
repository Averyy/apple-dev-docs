# MDLTextureChannelEncoding

**Framework**: Model I/O  
**Kind**: enum

Options for the data size and type of texel channel values, used by the [`channelEncoding`](mdltexture/channelencoding.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLTextureChannelEncoding
```

## Topics

### Constants
- [MDLTextureChannelEncoding.uInt8](mdltexturechannelencoding/uint8-swift.enum.case.md)
  Each channel value per texel is an 8-bit unsigned integer.
- [MDLTextureChannelEncoding.uInt16](mdltexturechannelencoding/uint16-swift.enum.case.md)
  Each channel value per texel is a 16-bit unsigned integer.
- [MDLTextureChannelEncoding.uInt24](mdltexturechannelencoding/uint24-swift.enum.case.md)
  Each channel value per texel is a 24-bit unsigned integer.
- [MDLTextureChannelEncoding.uInt32](mdltexturechannelencoding/uint32-swift.enum.case.md)
  Each channel value per texel is a 32-bit unsigned integer.
- [MDLTextureChannelEncoding.float16](mdltexturechannelencoding/float16.md)
  Each channel value per texel is a 16-bit floating-point value.
- [MDLTextureChannelEncoding.float32](mdltexturechannelencoding/float32.md)
  Each channel value per texel is a 32-bit floating-point value.
### Enumeration Cases
- [MDLTextureChannelEncoding.float16SR](mdltexturechannelencoding/float16sr.md)
### Initializers
- [init?(rawValue: Int)](mdltexturechannelencoding/init(rawvalue:).md)
### Type Properties
- [static var uint16: MDLTextureChannelEncoding](mdltexturechannelencoding/uint16-swift.type.property.md)
  Each channel value per texel is a 16-bit unsigned integer.
- [static var uint24: MDLTextureChannelEncoding](mdltexturechannelencoding/uint24-swift.type.property.md)
  Each channel value per texel is a 24-bit unsigned integer.
- [static var uint32: MDLTextureChannelEncoding](mdltexturechannelencoding/uint32-swift.type.property.md)
  Each channel value per texel is a 32-bit unsigned integer.
- [static var uint8: MDLTextureChannelEncoding](mdltexturechannelencoding/uint8-swift.type.property.md)
  Each channel value per texel is an 8-bit unsigned integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexturechannelencoding)*