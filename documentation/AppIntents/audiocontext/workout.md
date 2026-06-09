# workout

**Framework**: App Intents  
**Kind**: property

A workout session of any type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var workout: AudioContext { get }
```

#### Discussion

Use this to donate entities relevant to any workout, regardless of activity type or intensity.

You can donate entities to multiple workout contexts simultaneously. More specific contexts (e.g., a specific activity type) give the system stronger hints than broader ones (e.g., any workout). The system considers all matching entities and their relevance when determining what to suggest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiocontext/workout)*