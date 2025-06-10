# prewarm()

**Framework**: Foundation Models  
**Kind**: method

Requests that the system eagerly load the resources required for this session into memory.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func prewarm()
```

#### Discussion

Consider calling this method when you need to immediately use the session.

> **Note**: Calling this method does not guarantee that the system loads your assets immediately, particularly if your app is running in the background or the system is under load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/prewarm())*