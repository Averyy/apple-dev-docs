# requiresActivation

**Framework**: SwiftUI  
**Kind**: property

Prevents touch passthrough with the direct touch area until an assistive technology, such as VoiceOver, has activated the direct touch area through a user action, for example a double tap.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let requiresActivation: AccessibilityDirectTouchOptions
```

## See Also

- [static let silentOnTouch: AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions/silentontouch.md)
  Allows a direct touch area to immediately receive touch events without an assitive technology, such as VoiceOver, speaking. Appropriate for apps that provide direct audio feedback on touch that would conflict with speech feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions/requiresactivation)*