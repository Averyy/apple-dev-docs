# vDSP_int24

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A data structure that holds a 24-bit signed integer value.

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
struct vDSP_int24
```

```c
typedef struct { ... } vDSP_int24;
```

## Topics

### Initializers
- [init()](./vdsp_int24/init%28%29.md)
  Creates a 24-but signed integer value.
- [init(bytes: (UInt8, UInt8, UInt8))](./vdsp_int24/init%28bytes%29.md)
  Creates a 24-bit signed integer value from the specified bytes.
### Instance Properties
- [var bytes: (UInt8, UInt8, UInt8)](./vdsp_int24/bytes.md)
  The bytes that represent the value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### 24-bit integer to floating point conversion
- [struct vDSP_uint24](./vdsp_uint24.md)
  A data structure that holds a 24-bit unsigned integer value.
- [vDSP_vflt24](./vdsp_vflt24.md)
  Converts a vector of signed 24-bit integers to single-precision floating-point values.
- [vDSP_vfltu24](./vdsp_vfltu24.md)
  Converts a vector of unsigned 24-bit integers to single-precision floating-point values.
- [vDSP_vfltsm24](./vdsp_vfltsm24.md)
  Converts and scales a vector of signed 24-bit integers to single-precision floating-point values.
- [vDSP_vfltsmu24](./vdsp_vfltsmu24.md)
  Converts and scales a vector of unsigned 24-bit integers to single-precision floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_int24)*