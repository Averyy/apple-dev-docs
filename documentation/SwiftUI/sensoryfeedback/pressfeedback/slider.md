# slider

**Framework**: SwiftUI  
**Kind**: property

Indicates that a slider’s thumb has been pressed (touch down).

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
static let slider: SensoryFeedback.PressFeedback
```

#### Discussion

Slider controls should also play [`release(_:)`](sensoryfeedback/release(_:).md) with [`slider`](sensoryfeedback/releasefeedback/slider.md).

Only plays feedback on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/pressfeedback/slider)*