# toggle

**Framework**: SwiftUI  
**Kind**: property

Indicates that a toggle has been pressed (touch down).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let toggle: SensoryFeedback.PressFeedback
```

#### Discussion

Toggle controls should also play [`selection(_:)`](sensoryfeedback/selection(_:).md) with [`on`](sensoryfeedback/selectionfeedback/on.md) and [`off`](sensoryfeedback/selectionfeedback/off.md).

Only plays feedback on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/pressfeedback/toggle)*