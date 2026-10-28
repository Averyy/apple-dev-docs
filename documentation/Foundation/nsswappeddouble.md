# NSSwappedDouble

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Opaque structure containing endian-independent `double` value.

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
struct NSSwappedDouble
```

```c
typedef struct { ... } NSSwappedDouble;
```

## Overview

The fields of an [`NSSwappedDouble`](./nsswappeddouble.md) are private.

## Topics

### Initializers
- [init()](./nsswappeddouble/init%28%29.md)
- [init(v: UInt64)](./nsswappeddouble/init%28v%29.md)
### Instance Properties
- [var v: UInt64](./nsswappeddouble/v.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct NSSwappedFloat](./nsswappedfloat.md)
  Opaque type containing an endian-independent `float` value.
- [Byte Order](./byte-order-constants.md)
  Recognize constants that specify a byte-order format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsswappeddouble)*