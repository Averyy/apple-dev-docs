# accessibilityCustomContent

**Framework**: RealityKit  
**Kind**: property

The Custom Content API is useful for delivering accessibility information from complex data sets to your users in measured portions. Using this API allows you to leverage assistive technologies to present only the accessible content your app’s users need, when they need it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var accessibilityCustomContent: [AccessibilityComponent.CustomContent] { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/accessibilitycustomcontent-2tecl)*