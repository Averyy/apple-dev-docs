# needsInputModeSwitchKey

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the keyboard must display an input switcher key.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var needsInputModeSwitchKey: Bool { get }
```

#### Discussion

The input switcher key allows the user to switch between different keyboards. When this property is true, your custom keyboard should provide such a key.

## See Also

- [var hasFullAccess: Bool](uiinputviewcontroller/hasfullaccess.md)
  A Boolean value that indicates whether the keyboard has full access.
- [var hasDictationKey: Bool](uiinputviewcontroller/hasdictationkey.md)
  A Boolean value that indicates whether the keyboard has a dictation key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/needsinputmodeswitchkey)*