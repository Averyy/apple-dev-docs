# MTLFloatingPointConversionRoundingMode

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MTLFloatingPointConversionRoundingMode
```

```c
enum MTLFloatingPointConversionRoundingMode : NSInteger;
```

## Overview

The rounding mode for narrowing floating-point conversions.

Round-to-nearest-even (default). Standard IEEE 754 rounding mode.

Round-toward-zero.

## Topics

### Enumeration Cases
- [MTLFloatingPointConversionRoundingMode.toNearestEven](./mtlfloatingpointconversionroundingmode/tonearesteven.md)
- [MTLFloatingPointConversionRoundingMode.towardZero](./mtlfloatingpointconversionroundingmode/towardzero.md)
### Initializers
- [init?(rawValue: Int)](./mtlfloatingpointconversionroundingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfloatingpointconversionroundingmode)*