# image

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cursor’s image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

*Mac Catalyst*

```swift
var image: UIImage { get }
```

*macOS*

```swift
var image: NSImage { get }
```

*Mac Catalyst*

```objc
@property (strong, readonly) UIImage * image;
```

*macOS*

```objc
@property (strong, readonly) NSImage * image;
```

## Discussion

The cursor image or `nil` if none exists. Note that an `NSCursor` object is immutable: you cannot change its image after it’s created. Instead, use [`init(image:hotSpot:)`](./init%28image,hotspot%29.md) to create a new cursor with the new settings.

## See Also

### Related Documentation
- [init(image: UIImage, hotSpot: NSPoint)](./init%28image,hotspot%29.md)
  Initializes a cursor with the given image and hot spot.
### Setting cursor attributes
- [var hotSpot: NSPoint](./hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](./hide%28%29.md)
  Makes the current cursor invisible.
- [class func unhide()](./unhide%28%29.md)
  Negates an earlier call to [`hide()`](./hide%28%29.md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](./sethiddenuntilmousemoves%28_%29.md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/image)*