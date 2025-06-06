# setHiddenUntilMouseMoves(_:)

**Framework**: AppKit  
**Kind**: method

Sets whether the cursor is hidden until the mouse moves.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func setHiddenUntilMouseMoves(_ flag: Bool)
```

#### Discussion

Do not try to counter this method by invoking [`unhide()`](nscursor/unhide().md). The results are undefined.

## Parameters

- `flag`:   to hide the cursor until one of the following occurs:

## See Also

- [var image: UIImage](nscursor/image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](nscursor/hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](nscursor/hide.md)
  Makes the current cursor invisible.
- [class func unhide()](nscursor/unhide.md)
  Negates an earlier call to [`hide()`](nscursor/hide().md) by showing the current cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/sethiddenuntilmousemoves(_:))*