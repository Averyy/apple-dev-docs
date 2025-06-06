# CFConvertFloat32SwappedToHost(_:)

**Framework**: Core Foundation  
**Kind**: func

Converts a 32-bit float from a platform-independent format to the host’s native byte order.

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
func CFConvertFloat32SwappedToHost(_ arg: CFSwappedFloat32) -> Float32
```

#### Return Value

The real value in the host’s native format.

## Parameters

- `arg`: A structure holding the real value to convert.

## See Also

- [func CFByteOrderGetCurrent() -> CFByteOrder](cfbyteordergetcurrent().md)
  Returns the byte order of the current computer.
- [func CFConvertDoubleHostToSwapped(Double) -> CFSwappedFloat64](cfconvertdoublehosttoswapped(_:).md)
  Converts a 64-bit double from the host’s native byte order to a platform-independent format.
- [func CFConvertDoubleSwappedToHost(CFSwappedFloat64) -> Double](cfconvertdoubleswappedtohost(_:).md)
  Converts a 64-bit double from a platform-independent format to the host’s native byte order.
- [func CFConvertFloat32HostToSwapped(Float32) -> CFSwappedFloat32](cfconvertfloat32hosttoswapped(_:).md)
  Converts a 32-bit float from the host’s native byte order to a platform-independent format.
- [func CFConvertFloat64HostToSwapped(Float64) -> CFSwappedFloat64](cfconvertfloat64hosttoswapped(_:).md)
  Converts a 64-bit float from the host’s native byte order to a platform-independent format.
- [func CFConvertFloat64SwappedToHost(CFSwappedFloat64) -> Float64](cfconvertfloat64swappedtohost(_:).md)
  Converts a 64-bit float from a platform-independent format to the host’s native byte order.
- [func CFConvertFloatHostToSwapped(Float) -> CFSwappedFloat32](cfconvertfloathosttoswapped(_:).md)
  Converts a 32-bit float from the host’s native byte order to a platform-independent format.
- [func CFConvertFloatSwappedToHost(CFSwappedFloat32) -> Float](cfconvertfloatswappedtohost(_:).md)
  Converts a 32-bit float from a platform-independent format to the host’s native byte order.
- [func CFSwapInt16(UInt16) -> UInt16](cfswapint16(_:).md)
  Swaps the bytes of a 16-bit integer.
- [func CFSwapInt16BigToHost(UInt16) -> UInt16](cfswapint16bigtohost(_:).md)
  Converts a 16-bit integer from big-endian format to the host’s native byte order.
- [func CFSwapInt16HostToBig(UInt16) -> UInt16](cfswapint16hosttobig(_:).md)
  Converts a 16-bit integer from the host’s native byte order to big-endian format.
- [func CFSwapInt16HostToLittle(UInt16) -> UInt16](cfswapint16hosttolittle(_:).md)
  Converts a 16-bit integer from the host’s native byte order to little-endian format.
- [func CFSwapInt16LittleToHost(UInt16) -> UInt16](cfswapint16littletohost(_:).md)
  Converts a 16-bit integer from little-endian format to the host’s native byte order.
- [func CFSwapInt32(UInt32) -> UInt32](cfswapint32(_:).md)
  Swaps the bytes of a 32-bit integer.
- [func CFSwapInt32BigToHost(UInt32) -> UInt32](cfswapint32bigtohost(_:).md)
  Converts a 32-bit integer from big-endian format to the host’s native byte order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfconvertfloat32swappedtohost(_:))*