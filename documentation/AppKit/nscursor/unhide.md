# unhide()

**Framework**: AppKit  
**Kind**: method

Negates an earlier call to [`hide()`](nscursor/hide().md) by showing the current cursor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func unhide()
```

#### Discussion

Each invocation of `unhide` must be balanced by an invocation of [`hide()`](nscursor/hide().md) in order for the cursor display to be correct.

## See Also

- [var image: UIImage](nscursor/image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](nscursor/hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](nscursor/hide.md)
  Makes the current cursor invisible.
- [class func setHiddenUntilMouseMoves(Bool)](nscursor/sethiddenuntilmousemoves(_:).md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/unhide())*