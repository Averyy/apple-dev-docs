# predicateForActivitySummary(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches the activity summary for the specified day.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
class func predicateForActivitySummary(with dateComponents: DateComponents) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForActivitySummaryWithDateComponents:(NSDateComponents *) dateComponents;
```

## Return Value

A predicate for matching a single activity summary.

## Discussion

Use this convenience method to create a predicate that matches the activity summary for the specified day. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
let forDay = HKQuery.predicateForActivitySummaryWithDateComponents(day)
let explicitForDay = NSPredicate(format: "%K == %@", HKPredicateKeyPathDateComponents, day)
```

**Objective-C**:

```objc
NSPredicate *forDay =
[HKQuery predicateForActivitySummaryWithDateComponents: day];
 
NSPredicate *explicitforDay =
[NSPredicate predicateWithFormat:@"%K == %@",
 HKPredicateKeyPathDateComponents, day];
```

## Parameters

- `dateComponents`: Date components that uniquely identify the day as perceived by the user. This day may be longer or shorter than 24 hours (for example, if the user traveled across time zones).

  The date components must have a valid [`calendar`](../../Foundation/nsdatecomponents/calendar.md) property.

## See Also

### Related Documentation
- [let HKPredicateKeyPathDateComponents: String](../hkpredicatekeypathdatecomponents.md)
  The key path for accessing an activity summary’s date components.
### Creating activity summary predicates
- [class func predicate(forActivitySummariesBetweenStart: DateComponents, end: DateComponents) -> NSPredicate](./predicate%28foractivitysummariesbetweenstart,end%29.md)
  Returns a predicate for matching all the activity summaries that fall between the days identified by the start and end date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforactivitysummary(with:))*