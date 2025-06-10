# compareStartDate(with:)

**Framework**: EventKit  
**Kind**: method

Compares the start date of the receiving event with the start date of another event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func compareStartDate(with other: EKEvent) -> ComparisonResult
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Return Value

Returns [`ComparisonResult.orderedAscending`](https://developer.apple.com/documentation/Foundation/ComparisonResult/orderedAscending) if the start date of the receiver precedes the start date of `other`. Returns [`ComparisonResult.orderedSame`](https://developer.apple.com/documentation/Foundation/ComparisonResult/orderedSame) if the start dates of the two events are identical. Returns [`ComparisonResult.orderedDescending`](https://developer.apple.com/documentation/Foundation/ComparisonResult/orderedDescending) if the start date of the receiver comes after the start date of `other`.

#### Discussion

You can pass the selector for this method to the NSArray method [`sortedArray(using:)`](https://developer.apple.com/documentation/Foundation/NSArray/sortedArray(using:)-9nhh9) to create an array of events sorted by start date.

## Parameters

- `other`: The event to compare against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent/comparestartdate(with:))*