# keyEquivalentModifierMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The mask specifying the modifier keys for the button’s key equivalent.

**Availability**:
- macOS

## Declaration

```swift
var keyEquivalentModifierMask: NSEvent.ModifierFlags { get set }
```

```objc
@property NSEventModifierFlags keyEquivalentModifierMask;
```

#### Discussion

This property contains the mask specifying the modifier keys that are applied to the button’s key equivalent. Mask bits are defined in Modifier Flags. The only mask bits relevant in button key-equivalent modifier masks are `NSControlKeyMask`, `NSAlternateKeyMask`, and `NSCommandKeyMask`.

## See Also

### Accessing key equivalents
- [var keyEquivalent: String](./keyequivalent.md)
  The key-equivalent character of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/keyequivalentmodifiermask)*