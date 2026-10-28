# keyEquivalent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The button’s key-equivalent character.

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

The value of this property is the string that contains the key equivalent character of the button, or the empty string if one hasn’t been defined. Buttons don’t have a default key equivalent.

Setting this property redraws the button’s inside if it displays a key equivalent instead of an image. The key equivalent isn’t displayed if the image position is set to `NSNoImage`, `NSImageOnly`, or `NSImageOverlaps`; that is, the button must display both its title and its “image” (the key equivalent in this case), and they must not overlap.

To display a key equivalent on a button, set the image and alternate image to `nil`, then set the key equivalent, then set the image position.

## See Also

### Related Documentation
- [var image: NSImage?](../nscell/image.md)
  The image displayed by the cell, if any.
- [var alternateImage: NSImage?](./alternateimage.md)
  The image the button displays in its alternate state.
- [var imagePosition: NSControl.ImagePosition](./imageposition.md)
  The position of the button’s image relative to its title.
### Managing the Key Equivalent
- [var keyEquivalentModifierMask: NSEvent.ModifierFlags](./keyequivalentmodifiermask.md)
  The mask that identifies the modifier keys for the button’s key equivalent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/keyequivalent)*