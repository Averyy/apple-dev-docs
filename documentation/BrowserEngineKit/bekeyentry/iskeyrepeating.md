# isKeyRepeating

**Framework**: BrowserEngineKit  
**Kind**: property

Represents whether the event is repeating.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var isKeyRepeating: Bool { get }
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

For example, a continued press and hold on a key may result in its repeated insertion.

A Boolean value that indicates whether the person is holding the key down to repeat the key event.

## See Also

- [var state: BEKeyEntry.KeyPressState](bekeyentry/state.md)
  Type of the event, indicating whether it represents when the key is pressed or released.
- [BEKeyEntry.KeyPressState](bekeyentry/keypressstate.md)
  An enumeration that represents the possible states of a key-press in a keyboard event.
- [var timestamp: TimeInterval](bekeyentry/timestamp.md)
  Time at which the key event occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/iskeyrepeating)*