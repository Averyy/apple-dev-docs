# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method

Checks the button’s key equivalent against the specified event and, if they match, simulates the button being clicked.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performKeyEquivalent(with key: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the key equivalent in `anEvent` matches the button’s key equivalent; [`false`](https://developer.apple.com/documentation/Swift/false) if it does not. This method also returns [`false`](https://developer.apple.com/documentation/Swift/false) if the button is blocked by a modal panel or the button is disabled.

#### Discussion

If the character in `anEvent` matches the button’s key equivalent, and the modifier flags in `anEvent` match the key-equivalent modifier mask, [`performKeyEquivalent(with:)`](nsbutton/performkeyequivalent(with:).md) simulates the user clicking the button and returning [`true`](https://developer.apple.com/documentation/Swift/true). Otherwise, [`performKeyEquivalent(with:)`](nsbutton/performkeyequivalent(with:).md) does nothing and returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `key`: The event containing the key equivalent.

## See Also

- [var keyEquivalent: String](nsbutton/keyequivalent.md)
  The key-equivalent character of the button.
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](nsbutton/keyequivalentmodifiermask.md)
  The mask specifying the modifier keys for the button’s key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/performkeyequivalent(with:))*