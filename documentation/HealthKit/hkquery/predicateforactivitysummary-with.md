# predicateForActivitySummary(with:)

**Framework**: HealthKit  
**Kind**: method

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

#### Return Value

A predicate for matching a single activity summary.

#### Discussion

Use this convenience method to create a predicate that matches the activity summary for the specified day. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

## Parameters

- `dateComponents`: The date components must have a valid   property.

## See Also

- [let HKPredicateKeyPathDateComponents: String](hkpredicatekeypathdatecomponents.md)
  The key path for accessing an activity summary’s date components.
- [class func predicate(forActivitySummariesBetweenStart: DateComponents, end: DateComponents) -> NSPredicate](hkquery/predicate(foractivitysummariesbetweenstart:end:).md)
  Returns a predicate for matching all the activity summaries that fall between the days identified by the start and end date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforactivitysummary(with:))*