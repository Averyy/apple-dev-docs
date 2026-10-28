# hotSpot

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSPoint hotSpot;
```

## Discussion

The hot spot precisely determines the click location within the cursor’s image. Using its flipped coordinate system, you calculate the hot spot in points with the top-left corner acting as the origin. For example, the arrow cursor’s hot spot is at the intersection of its left and right edges, which is inset 4pts from the image’s corner to account for the arrow’s stroke and shadow.

![A diagram showing an arrow cursor that points up and to the left. At the tip of the arrow, inset slightly, is a cross hair pointing to the cursor’s hot spot.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-4311497@2x.png)

Note that an `NSCursor` object is immutable: you can’t change its hot spot after it’s created. Instead, use [`init(image:hotSpot:)`](./init%28image,hotspot%29.md) to create a new cursor with the new settings.

## See Also

### Related Documentation
- [init(image: UIImage, hotSpot: NSPoint)](./init%28image,hotspot%29.md)
  Initializes a cursor with the given image and hot spot.
### Setting cursor attributes
- [var image: UIImage](./image.md)
  The cursor’s image.
- [class func hide()](./hide%28%29.md)
  Makes the current cursor invisible.
- [class func unhide()](./unhide%28%29.md)
  Negates an earlier call to [`hide()`](./hide%28%29.md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](./sethiddenuntilmousemoves%28_%29.md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/hotspot)*