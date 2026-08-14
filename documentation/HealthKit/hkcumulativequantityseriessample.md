# HKCumulativeQuantitySeriesSample

**Framework**: HealthKit  
**Kind**: class

A sample representing a series of cumulative quantity values.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class HKCumulativeQuantitySeriesSample
```

## Topics

### Accessing Data
- [var sum: HKQuantity](hkcumulativequantityseriessample/sum.md)
  The sum of all the quantities in the series.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathSum: String](hkpredicatekeypathsum.md)
  The key path for accessing the sum of a quantity series inside a predicate format string.

## Relationships

### Inherits From
- [HKCumulativeQuantitySample](hkcumulativequantitysample.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class HKQuantitySeriesSampleQuery](hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcumulativequantityseriessample)*