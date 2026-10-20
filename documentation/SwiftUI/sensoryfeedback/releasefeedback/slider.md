# slider

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

Indicates that a slider’s thumb has been released (touch up).

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
static let slider: SensoryFeedback.ReleaseFeedback
```

#### Discussion

Slider controls should also play [`press(_:)`](../press%28_%29.md) with [`slider`](../pressfeedback/slider.md).

Only plays feedback on visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sensoryfeedback/releasefeedback/slider)*