# Byte-Order Utilities

**Framework**: Core Foundation  
**Role**: API Collection

#### Overview

When handling binary data transmitted or shared across platforms, you need be concerned with how each platform stores numerical values. A platform stores values either in big-endian or little-endian format. On big-endian machines, such as PowerPC machines, values are stored with the most-significant bytes first in memory; on little-endian machines, such as Pentium machines, values are stored with the least-significant bytes first. A multibyte value transmitted to a platform with a different format will be misinterpreted if it is not converted properly by one of the computers.

You identify the native format of the current platform using the [`CFByteOrderGetCurrent()`](./cfbyteordergetcurrent%28%29.md) function. Use functions such as [`CFSwapInt32BigToHost(_:)`](./cfswapint32bigtohost%28_%29.md) and [`CFConvertFloat32HostToSwapped(_:)`](./cfconvertfloat32hosttoswapped%28_%29.md) to convert values between different byte order formats.

## Topics

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
- [func CFConvertFloatHostToSwapped(Float) -> CFSwappedFloat32](./cfconvertfloathosttoswapped%28_%29.md)
  Converts a 32-bit float from the host’s native byte order to a platform-independent format.
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
- [func CFSwapInt32HostToBig(UInt32) -> UInt32](./cfswapint32hosttobig%28_%29.md)
  Converts a 32-bit integer from the host’s native byte order to big-endian format.
- [func CFSwapInt32HostToLittle(UInt32) -> UInt32](./cfswapint32hosttolittle%28_%29.md)
  Converts a 32-bit integer from the host’s native byte order to little-endian format.
- [func CFSwapInt32LittleToHost(UInt32) -> UInt32](./cfswapint32littletohost%28_%29.md)
  Converts a 32-bit integer from little-endian format to the host’s native byte order.
- [func CFSwapInt64(UInt64) -> UInt64](./cfswapint64%28_%29.md)
  Swaps the bytes of a 64-bit integer.
- [func CFSwapInt64BigToHost(UInt64) -> UInt64](./cfswapint64bigtohost%28_%29.md)
  Converts a 64-bit integer from big-endian format to the host’s native byte order.
- [func CFSwapInt64HostToBig(UInt64) -> UInt64](./cfswapint64hosttobig%28_%29.md)
  Converts a 64-bit integer from the host’s native byte order to big-endian format.
- [func CFSwapInt64HostToLittle(UInt64) -> UInt64](./cfswapint64hosttolittle%28_%29.md)
  Converts a 64-bit integer from the host’s native byte order to little-endian format.
- [func CFSwapInt64LittleToHost(UInt64) -> UInt64](./cfswapint64littletohost%28_%29.md)
  Converts a 64-bit integer from little-endian format to the host’s native byte order.
### Data Types
- [struct CFSwappedFloat32](./cfswappedfloat32.md)
  Structure holding a 32-bit float value in a platform-independentbyte order.
- [struct CFSwappedFloat64](./cfswappedfloat64.md)
  Structure holding a 64-bit float value in a platform-independentbyte order.
### Constants
- [typealias CFByteOrder](./cfbyteorder.md)
  Flags that identify byte order.

## See Also

### Related Documentation
- [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)
### Utilities
- [Base Utilities](./base-utilities.md)
- [Core Foundation URL Access Utilities](./core-foundation-url-access-utilities.md)
- [Preferences Utilities](./preferences-utilities.md)
- [Socket Name Server Utilities](./socket-name-server-utilities.md)
- [Time Utilities](./time-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/byte-order-utilities)*