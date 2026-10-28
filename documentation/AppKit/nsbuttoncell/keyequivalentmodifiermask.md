# keyEquivalentModifierMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The mask that identifies the modifier keys for the button’s key equivalent.

**Availability**:
- macOS

## Declaration

```swift
var keyEquivalentModifierMask: NSEvent.ModifierFlags { get set }
```

```objc
@property NSEventModifierFlags keyEquivalentModifierMask;
```

## Discussion

The value of this property is a mask that indicates the modifier keys that are applied to the button’s key equivalent. Mask bits are defined in `NSEvent.h`. The only mask bits that are relevant in button key-equivalent modifier masks are `NSControlKeyMask`, `NSAlternateKeyMask`, and `NSCommandKeyMask` bits.

## See Also

### Managing the Key Equivalent
- [var keyEquivalent: String](./keyequivalent.md)
  The button’s key-equivalent character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/keyequivalentmodifiermask)*