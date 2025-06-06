# predicateForSamples(withStart:end:options:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for samples whose start and end dates fall within the specified time interval.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func predicateForSamples(withStart startDate: Date?, end endDate: Date?, options: HKQueryOptions = []) -> NSPredicate
```

#### Return Value

A predicate for samples whose start and end dates fall within the specified time interval. This predicate works only with samples.

#### Discussion

Use this convenience method to create a predicate that compares a sample’s start and end dates with a specified time interval. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

## Parameters

- `startDate`: The start date for the target time interval.
- `endDate`: The end date for the target time interval.
- `options`: A constant that specifies how the sample’s start and end date are compared with the target time interval. For a list of possible values, see  .

## See Also

- [let HKPredicateKeyPathEndDate: String](hkpredicatekeypathenddate.md)
  The key path for accessing the sample’s end date.
- [let HKPredicateKeyPathStartDate: String](hkpredicatekeypathstartdate.md)
  The key path for accessing the sample’s start date.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [struct HKQueryOptions](hkqueryoptions.md)
  Constants that describe how a sample’s time period overlaps with the target time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforsamples(withstart:end:options:))*