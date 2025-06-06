# init(minimumInterval:paused:)

**Framework**: SwiftUI  
**Kind**: init

Create a pausable schedule of dates updating at a frequency no more quickly than the provided interval.

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
init(minimumInterval: Double? = nil, paused: Bool = false)
```

## Parameters

- `minimumInterval`: The minimum interval to update the schedule at.   Pass nil to let the system pick an appropriate update interval.
- `paused`: If the schedule should stop generating updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animationtimelineschedule/init(minimuminterval:paused:))*