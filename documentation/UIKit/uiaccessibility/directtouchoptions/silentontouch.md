# silentOnTouch

**Framework**: UIKit  
**Kind**: property

Allows a direct touch area to immediately receive touch events without triggering VoiceOver audio.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var silentOnTouch: UIAccessibility.DirectTouchOptions { get }
```

#### Discussion

You may want a user interface element that, when a person interacts with it, provides audio feedback that would conflict with VoiceOver. In a music creation app, for example, you can designate the keyboard as “silent on touch,” so that VoiceOver doesn’t compete with the keyboard sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/directtouchoptions/silentontouch)*