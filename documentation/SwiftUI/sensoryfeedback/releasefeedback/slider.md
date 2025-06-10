# slider

**Framework**: SwiftUI  
**Kind**: property

Indicates that a slider’s thumb has been released (touch up).

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
static let slider: SensoryFeedback.ReleaseFeedback
```

#### Discussion

Slider controls should also play [`press(_:)`](sensoryfeedback/press(_:).md) with [`slider`](sensoryfeedback/pressfeedback/slider.md).

Only plays feedback on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/releasefeedback/slider)*