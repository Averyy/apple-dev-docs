# image

**Framework**: AppKit  
**Kind**: property

The cursor’s image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
var image: NSImage { get }
```

#### Discussion

The cursor image or `nil` if none exists. Note that an `NSCursor` object is immutable: you cannot change its image after it’s created. Instead, use [`init(image:hotSpot:)`](nscursor/init(image:hotspot:).md) to create a new cursor with the new settings.

## See Also

- [init(image: UIImage, hotSpot: NSPoint)](nscursor/init(image:hotspot:).md)
  Initializes a cursor with the given image and hot spot.
- [var hotSpot: NSPoint](nscursor/hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](nscursor/hide.md)
  Makes the current cursor invisible.
- [class func unhide()](nscursor/unhide.md)
  Negates an earlier call to [`hide()`](nscursor/hide().md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](nscursor/sethiddenuntilmousemoves(_:).md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/image)*