# NSSwappedFloat

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Opaque type containing an endian-independent `float` value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSSwappedFloat
```

```c
typedef struct { ... } NSSwappedFloat;
```

## Overview

The fields of an [`NSSwappedFloat`](./nsswappedfloat.md) are private.

## Topics

### Initializers
- [init()](./nsswappedfloat/init%28%29.md)
- [init(v: UInt32)](./nsswappedfloat/init%28v%29.md)
### Instance Properties
- [var v: UInt32](./nsswappedfloat/v.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct NSSwappedDouble](./nsswappeddouble.md)
  Opaque structure containing endian-independent `double` value.
- [Byte Order](./byte-order-constants.md)
  Recognize constants that specify a byte-order format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsswappedfloat)*