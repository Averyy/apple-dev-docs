# HKQueryOptions

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum HKQueryOptions : NSUInteger;
```

## Topics

### Constants
- [static var strictStartDate: HKQueryOptions](./hkqueryoptions/strictstartdate.md)
  The sample’s start time must fall within the target time period.
- [static var strictEndDate: HKQueryOptions](./hkqueryoptions/strictenddate.md)
  The sample’s end time must fall within the target time period.
### Initializers
- [init(rawValue: UInt)](./hkqueryoptions/init%28rawvalue%29.md)
  Returns a newly initialized query option using the provided integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Creating sample predicates
- [class func predicateForSamples(withStart: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](./hkquery/predicateforsamples%28withstart,end,options%29.md)
  Returns a predicate for samples whose start and end dates fall within the specified time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryoptions)*