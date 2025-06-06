# silentOnTouch

**Framework**: SwiftUI  
**Kind**: property

Allows a direct touch area to immediately receive touch events without an assitive technology, such as VoiceOver, speaking. Appropriate for apps that provide direct audio feedback on touch that would conflict with speech feedback.

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
static let silentOnTouch: AccessibilityDirectTouchOptions
```

## See Also

- [static let requiresActivation: AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions/requiresactivation.md)
  Prevents touch passthrough with the direct touch area until an assistive technology, such as VoiceOver, has activated the direct touch area through a user action, for example a double tap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions/silentontouch)*