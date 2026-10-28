# keyEquivalent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item’s unmodified key equivalent.

**Availability**:
- macOS

## Declaration

```swift
var keyEquivalent: String { get set }
```

```objc
@property (copy) NSString * keyEquivalent;
```

## Discussion

If you want to specify the Backspace key as the key equivalent for a menu item, use a single character string with [`NSBackspaceCharacter`](../nsbackspacecharacter.md) (defined in `NSText.h` as `0x08`) and for the Forward Delete key, use [`NSDeleteCharacter`](../nsdeletecharacter.md) (defined in `NSText.h` as `0x7F`). Note that these are not the same characters you get from an [`NSEvent`](../nsevent.md) key-down event when pressing those keys.

## See Also

### Related Documentation
- [var userKeyEquivalent: String](./userkeyequivalent.md)
  The user-assigned key equivalent for the menu item.
- [- mnemonic](./mnemonic.md)
  Returns the character in the menu item title that appears underlined for use as a mnemonic.
- [- setMnemonicLocation:](./setmnemoniclocation_.md)
  Sets the character of the menu item title at location that is to be underlined.
### Managing key equivalents
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](./keyequivalentmodifiermask.md)
  The menu item’s keyboard equivalent modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/keyequivalent)*