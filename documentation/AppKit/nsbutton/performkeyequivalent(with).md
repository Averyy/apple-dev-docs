# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Checks the button’s key equivalent against the specified event and, if they match, simulates the button being clicked.

**Availability**:
- macOS

## Declaration

```swift
func performKeyEquivalent(with key: NSEvent) -> Bool
```

```objc
- (BOOL) performKeyEquivalent:(NSEvent *) key;
```

## Return Value

[`true`](../../Swift/true.md) if the key equivalent in `anEvent` matches the button’s key equivalent; [`false`](../../Swift/false.md) if it does not. This method also returns [`false`](../../Swift/false.md) if the button is blocked by a modal panel or the button is disabled.

## Discussion

If the character in `anEvent` matches the button’s key equivalent, and the modifier flags in `anEvent` match the key-equivalent modifier mask, [`performKeyEquivalent(with:)`](./performkeyequivalent%28with%29.md) simulates the user clicking the button and returning [`true`](../../Swift/true.md). Otherwise, [`performKeyEquivalent(with:)`](./performkeyequivalent%28with%29.md) does nothing and returns [`false`](../../Swift/false.md).

## Parameters

- `key`: The event containing the key equivalent.

## See Also

### Related Documentation
- [var keyEquivalent: String](./keyequivalent.md)
  The key-equivalent character of the button.
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](./keyequivalentmodifiermask.md)
  The mask specifying the modifier keys for the button’s key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/performkeyequivalent(with:))*