# CFConvertFloatHostToSwapped(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Converts a 32-bit float from the host’s native byte order to a platform-independent format.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFConvertFloatHostToSwapped(_ arg: Float) -> CFSwappedFloat32
```

```c
static CFSwappedFloat32 CFConvertFloatHostToSwapped(float arg);
```

#### Return Value

A structure holding the real value in a canonical byte order.

## Parameters

- `arg`: The real value to convert.

## See Also

### Core Foundation Byte Order Utilities Miscellaneous Functions
- [func CFByteOrderGetCurrent() -> CFByteOrder](./cfbyteordergetcurrent%28%29.md)
  Returns the byte order of the current computer.
- [func CFConvertDoubleHostToSwapped(Double) -> CFSwappedFloat64](./cfconvertdoublehosttoswapped%28_%29.md)
  Converts a 64-bit double from the host’s native byte order to a platform-independent format.
- [func CFConvertDoubleSwappedToHost(CFSwappedFloat64) -> Double](./cfconvertdoubleswappedtohost%28_%29.md)
  Converts a 64-bit double from a platform-independent format to the host’s native byte order.
- [func CFConvertFloat32HostToSwapped(Float32) -> CFSwappedFloat32](./cfconvertfloat32hosttoswapped%28_%29.md)
  Converts a 32-bit float from the host’s native byte order to a platform-independent format.
- [func CFConvertFloat32SwappedToHost(CFSwappedFloat32) -> Float32](./cfconvertfloat32swappedtohost%28_%29.md)
  Converts a 32-bit float from a platform-independent format to the host’s native byte order.
- [func CFConvertFloat64HostToSwapped(Float64) -> CFSwappedFloat64](./cfconvertfloat64hosttoswapped%28_%29.md)
  Converts a 64-bit float from the host’s native byte order to a platform-independent format.
- [func CFConvertFloat64SwappedToHost(CFSwappedFloat64) -> Float64](./cfconvertfloat64swappedtohost%28_%29.md)
  Converts a 64-bit float from a platform-independent format to the host’s native byte order.
- [func CFConvertFloatSwappedToHost(CFSwappedFloat32) -> Float](./cfconvertfloatswappedtohost%28_%29.md)
  Converts a 32-bit float from a platform-independent format to the host’s native byte order.
- [func CFSwapInt16(UInt16) -> UInt16](./cfswapint16%28_%29.md)
  Swaps the bytes of a 16-bit integer.
- [func CFSwapInt16BigToHost(UInt16) -> UInt16](./cfswapint16bigtohost%28_%29.md)
  Converts a 16-bit integer from big-endian format to the host’s native byte order.
- [func CFSwapInt16HostToBig(UInt16) -> UInt16](./cfswapint16hosttobig%28_%29.md)
  Converts a 16-bit integer from the host’s native byte order to big-endian format.
- [func CFSwapInt16HostToLittle(UInt16) -> UInt16](./cfswapint16hosttolittle%28_%29.md)
  Converts a 16-bit integer from the host’s native byte order to little-endian format.
- [func CFSwapInt16LittleToHost(UInt16) -> UInt16](./cfswapint16littletohost%28_%29.md)
  Converts a 16-bit integer from little-endian format to the host’s native byte order.
- [func CFSwapInt32(UInt32) -> UInt32](./cfswapint32%28_%29.md)
  Swaps the bytes of a 32-bit integer.
- [func CFSwapInt32BigToHost(UInt32) -> UInt32](./cfswapint32bigtohost%28_%29.md)
  Converts a 32-bit integer from big-endian format to the host’s native byte order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfconvertfloathosttoswapped(_:))*