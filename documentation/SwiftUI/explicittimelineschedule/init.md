# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a schedule composed of an explicit sequence of dates.

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
init(_ dates: Entries)
```

#### Discussion

Use the [`entries(from:mode:)`](explicittimelineschedule/entries(from:mode:).md) method to get the sequence of dates.

## Parameters

- `dates`: The sequence of dates at which a timeline view   updates. Use a monotonically increasing sequence of dates,   and ensure that at least one is in the future.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/explicittimelineschedule/init(_:))*