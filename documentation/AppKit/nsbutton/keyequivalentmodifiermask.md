# keyEquivalentModifierMask

**Framework**: AppKit  
**Kind**: property

The mask specifying the modifier keys for the button’s key equivalent.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var keyEquivalentModifierMask: NSEvent.ModifierFlags { get set }
```

#### Discussion

This property contains the mask specifying the modifier keys that are applied to the button’s key equivalent. Mask bits are defined in Modifier Flags. The only mask bits relevant in button key-equivalent modifier masks are `NSControlKeyMask`, `NSAlternateKeyMask`, and `NSCommandKeyMask`.

## See Also

- [var keyEquivalent: String](nsbutton/keyequivalent.md)
  The key-equivalent character of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/keyequivalentmodifiermask)*