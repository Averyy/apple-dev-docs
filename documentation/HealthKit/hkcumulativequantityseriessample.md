# HKCumulativeQuantitySeriesSample

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A sample representing a series of cumulative quantity values.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0 (renamed: HKCumulativeQuantitySample)
- iPadOS 12.0+ - Deprecated in 13.0 (renamed: HKCumulativeQuantitySample)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: HKCumulativeQuantitySample)
- macOS
- visionOS 1.0+ - Deprecated in 1.0 (renamed: HKCumulativeQuantitySample)
- watchOS 5.0+ - Deprecated in 6.0 (renamed: HKCumulativeQuantitySample)

> **Deprecated**: Use [`HKCumulativeQuantitySample`](./hkcumulativequantitysample.md) instead.

## Declaration

```swift
class HKCumulativeQuantitySeriesSample
```

```objc
@interface HKCumulativeQuantitySeriesSample : HKCumulativeQuantitySample
```

## Topics

### Accessing Data
- [var sum: HKQuantity](./hkcumulativequantityseriessample/sum.md)
  The sum of all the quantities in the series.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathSum: String](./hkpredicatekeypathsum.md)
  The key path for accessing the sum of a quantity series inside a predicate format string.

## Relationships

### Inherits From
- [HKCumulativeQuantitySample](./hkcumulativequantitysample.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [class HKQuantitySeriesSampleQuery](./hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcumulativequantityseriessample)*