# vDSP_uint24

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A data structure that holds a 24-bit unsigned integer value.

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
struct vDSP_uint24
```

```c
typedef struct { ... } vDSP_uint24;
```

## Topics

### Initializers
- [init()](./vdsp_uint24/init%28%29.md)
  Creates a 24-but unsigned integer value.
- [init(bytes: (UInt8, UInt8, UInt8))](./vdsp_uint24/init%28bytes%29.md)
  Creates a 24-bit unsigned integer value from the specified bytes.
### Instance Properties
- [var bytes: (UInt8, UInt8, UInt8)](./vdsp_uint24/bytes.md)
  The bytes that represent the value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### 24-bit integer to floating point conversion
- [struct vDSP_int24](./vdsp_int24.md)
  A data structure that holds a 24-bit signed integer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_uint24)*