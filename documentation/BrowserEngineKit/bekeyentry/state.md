# state

**Framework**: BrowserEngineKit  
**Kind**: property

Type of the event, indicating whether it represents when the key is pressed or released.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var state: BEKeyEntry.KeyPressState { get }
```

#### Discussion

Whether the key is pressed or released.

## See Also

- [BEKeyEntry.KeyPressState](bekeyentry/keypressstate.md)
  An enumeration that represents the possible states of a key-press in a keyboard event.
- [var isKeyRepeating: Bool](bekeyentry/iskeyrepeating.md)
  Represents whether the event is repeating.
- [var timestamp: TimeInterval](bekeyentry/timestamp.md)
  Time at which the key event occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/state)*