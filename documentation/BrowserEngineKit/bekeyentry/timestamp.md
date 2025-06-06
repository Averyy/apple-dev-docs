# timestamp

**Framework**: BrowserEngineKit  
**Kind**: property

Time at which the key event occurred.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

#### Discussion

The time at which the key event occurs.

## See Also

- [var state: BEKeyEntry.KeyPressState](bekeyentry/state.md)
  Type of the event, indicating whether it represents when the key is pressed or released.
- [BEKeyEntry.KeyPressState](bekeyentry/keypressstate.md)
  An enumeration that represents the possible states of a key-press in a keyboard event.
- [var isKeyRepeating: Bool](bekeyentry/iskeyrepeating.md)
  Represents whether the event is repeating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/timestamp)*