# Entries

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Required**: Yes

The sequence of dates within a schedule.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
associatedtype Entries : Sequence where Self.Entries.Element == Date
```

#### Discussion

The [`entries(from:mode:)`](timelineschedule/entries(from:mode:).md) method returns a value of this type, which is a [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) of dates in ascending order. A [`TimelineView`](timelineview.md) that you create with a schedule updates its content at the moments in time corresponding to the dates included in the sequence.

## See Also

- [func entries(from: Date, mode: Self.Mode) -> Self.Entries](timelineschedule/entries(from:mode:).md)
  Provides a sequence of dates starting around a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/timelineschedule/entries)*