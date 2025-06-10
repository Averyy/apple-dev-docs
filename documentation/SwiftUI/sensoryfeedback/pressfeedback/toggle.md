# toggle

**Framework**: SwiftUI  
**Kind**: property

Indicates that a toggle has been pressed (touch down).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static let toggle: SensoryFeedback.PressFeedback
```

#### Discussion

Toggle controls should also play [`selection(_:)`](sensoryfeedback/selection(_:).md) with [`on`](sensoryfeedback/selectionfeedback/on.md) and [`off`](sensoryfeedback/selectionfeedback/off.md).

Only plays feedback on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/pressfeedback/toggle)*