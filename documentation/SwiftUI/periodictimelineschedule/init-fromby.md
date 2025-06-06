# init(from:by:)

**Framework**: SwiftUI  
**Kind**: init

Creates a periodic update schedule.

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
init(from startDate: Date, by interval: TimeInterval)
```

#### Discussion

Use the [`entries(from:mode:)`](periodictimelineschedule/entries(from:mode:).md) method to get the sequence of dates.

## Parameters

- `startDate`: The date on which to start the sequence.
- `interval`: The time interval between successive sequence entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/periodictimelineschedule/init(from:by:))*