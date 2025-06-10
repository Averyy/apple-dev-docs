# HKQueryOptions

**Framework**: HealthKit  
**Kind**: struct

Constants that describe how a sample’s time period overlaps with the target time period.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct HKQueryOptions
```

## Topics

### Constants
- [static var strictStartDate: HKQueryOptions](hkqueryoptions/strictstartdate.md)
  The sample’s start time must fall within the target time period.
- [static var strictEndDate: HKQueryOptions](hkqueryoptions/strictenddate.md)
  The sample’s end time must fall within the target time period.
### Initializers
- [init(rawValue: UInt)](hkqueryoptions/init(rawvalue:).md)
  Returns a newly initialized query option using the provided integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func predicateForSamples(withStart: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](hkquery/predicateforsamples(withstart:end:options:).md)
  Returns a predicate for samples whose start and end dates fall within the specified time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryoptions)*