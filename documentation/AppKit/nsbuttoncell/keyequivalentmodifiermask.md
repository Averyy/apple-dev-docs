# keyEquivalentModifierMask

**Framework**: AppKit  
**Kind**: property

The mask that identifies the modifier keys for the button’s key equivalent.

**Availability**:
- macOS ?+

## Declaration

```swift
var keyEquivalentModifierMask: NSEvent.ModifierFlags { get set }
```

#### Discussion

The value of this property is a mask that indicates the modifier keys that are applied to the button’s key equivalent. Mask bits are defined in `NSEvent.h`. The only mask bits that are relevant in button key-equivalent modifier masks are `NSControlKeyMask`, `NSAlternateKeyMask`, and `NSCommandKeyMask` bits.

## See Also

- [var keyEquivalent: String](nsbuttoncell/keyequivalent.md)
  The button’s key-equivalent character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/keyequivalentmodifiermask)*