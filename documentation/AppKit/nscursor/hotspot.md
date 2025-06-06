# hotSpot

**Framework**: AppKit  
**Kind**: property

The position of the click location within the cursor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
var hotSpot: NSPoint { get }
```

#### Discussion

The hot spot precisely determines the click location within the cursor’s image. Using its flipped coordinate system, you calculate the hot spot in points with the top-left corner acting as the origin. For example, the arrow cursor’s hot spot is at the intersection of its left and right edges, which is inset 4pts from the image’s corner to account for the arrow’s stroke and shadow.

![A diagram showing an arrow cursor that points up and to the left. At the tip of the arrow, inset slightly, is a cross hair pointing to the cursor’s hot spot.](https://docs-assets.developer.apple.com/published/e5091aa5be2b52dcadf2d52c1d016a30/media-4311497%402x.png)

Note that an `NSCursor` object is immutable: you can’t change its hot spot after it’s created. Instead, use [`init(image:hotSpot:)`](nscursor/init(image:hotspot:).md) to create a new cursor with the new settings.

## See Also

- [init(image: UIImage, hotSpot: NSPoint)](nscursor/init(image:hotspot:).md)
  Initializes a cursor with the given image and hot spot.
- [var image: UIImage](nscursor/image.md)
  The cursor’s image.
- [class func hide()](nscursor/hide.md)
  Makes the current cursor invisible.
- [class func unhide()](nscursor/unhide.md)
  Negates an earlier call to [`hide()`](nscursor/hide().md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](nscursor/sethiddenuntilmousemoves(_:).md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/hotspot)*