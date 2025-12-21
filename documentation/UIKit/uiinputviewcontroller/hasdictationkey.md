# hasDictationKey

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the keyboard has a dictation key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hasDictationKey: Bool { get set }
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system dictation key is in a disabled state.

## See Also

- [var needsInputModeSwitchKey: Bool](uiinputviewcontroller/needsinputmodeswitchkey.md)
  A Boolean value that indicates whether the keyboard must display an input switcher key.
- [var hasFullAccess: Bool](uiinputviewcontroller/hasfullaccess.md)
  A Boolean value that indicates whether the keyboard has full access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/hasdictationkey)*