# keyEquivalent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The key-equivalent character of the button.

**Availability**:
- macOS

## Declaration

```swift
var keyEquivalent: String { get set }
```

```objc
@property (copy) NSString * keyEquivalent;
```

#### Discussion

This property contains the button’s key equivalent, or the empty string if no equivalent has been defined. Buttons don’t have a default key equivalent.

If you set a key equivalent instead of an image, the button’s interior is redrawn. However, the key equivalent isn’t displayed if the image position is set to `NSNoImage`, `NSImageOnly`, or `NSImageOverlaps`; that is, the button must display both its title and its “image” (which is the key equivalent in this case), and they must not overlap.

To display a key equivalent on a button, set the image and alternate image to `nil`, set the key equivalent, and then set the image position.

## See Also

### Related Documentation
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Checks the button’s key equivalent against the specified event and, if they match, simulates the button being clicked.
- [var keyEquivalentFont: NSFont?](../nsbuttoncell/keyequivalentfont.md)
  The font used to draw the button’s key equivalent.
### Accessing key equivalents
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](./keyequivalentmodifiermask.md)
  The mask specifying the modifier keys for the button’s key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/keyequivalent)*