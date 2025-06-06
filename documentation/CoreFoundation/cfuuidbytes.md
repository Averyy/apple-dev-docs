# CFUUIDBytes

**Framework**: Core Foundation  
**Kind**: struct

A 128-bit struct that represents a UUID as raw bytes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFUUIDBytes
```

#### Overview

This structure can be obtained from a CFUUID object using the [`CFUUIDGetUUIDBytes(_:)`](cfuuidgetuuidbytes(_:).md) function. This structure can be passed to functions that expect a raw UUID.

## Topics

### Initializers
- [init()](cfuuidbytes/init.md)
- [init(byte0: UInt8, byte1: UInt8, byte2: UInt8, byte3: UInt8, byte4: UInt8, byte5: UInt8, byte6: UInt8, byte7: UInt8, byte8: UInt8, byte9: UInt8, byte10: UInt8, byte11: UInt8, byte12: UInt8, byte13: UInt8, byte14: UInt8, byte15: UInt8)](cfuuidbytes/init(byte0:byte1:byte2:byte3:byte4:byte5:byte6:byte7:byte8:byte9:byte10:byte11:byte12:byte13:byte14:byte15:).md)
### Instance Properties
- [var byte0: UInt8](cfuuidbytes/byte0.md)
  The first byte.
- [var byte1: UInt8](cfuuidbytes/byte1.md)
  The second byte.
- [var byte10: UInt8](cfuuidbytes/byte10.md)
  The eleventh byte.
- [var byte11: UInt8](cfuuidbytes/byte11.md)
  The twelfth byte.
- [var byte12: UInt8](cfuuidbytes/byte12.md)
  The thirteenth byte.
- [var byte13: UInt8](cfuuidbytes/byte13.md)
  The fourteenth byte.
- [var byte14: UInt8](cfuuidbytes/byte14.md)
  The fifteenth byte.
- [var byte15: UInt8](cfuuidbytes/byte15.md)
  The sixteenth byte.
- [var byte2: UInt8](cfuuidbytes/byte2.md)
  The third byte.
- [var byte3: UInt8](cfuuidbytes/byte3.md)
  The fourth byte.
- [var byte4: UInt8](cfuuidbytes/byte4.md)
  The fifth byte.
- [var byte5: UInt8](cfuuidbytes/byte5.md)
  The sixth byte.
- [var byte6: UInt8](cfuuidbytes/byte6.md)
  The seventh byte.
- [var byte7: UInt8](cfuuidbytes/byte7.md)
  The eighth byte.
- [var byte8: UInt8](cfuuidbytes/byte8.md)
  The ninth byte.
- [var byte9: UInt8](cfuuidbytes/byte9.md)
  The tenth byte.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidbytes)*