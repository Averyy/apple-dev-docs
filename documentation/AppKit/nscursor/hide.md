# hide()

**Framework**: AppKit  
**Kind**: method

Makes the current cursor invisible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func hide()
```

#### Discussion

If another cursor becomes current, that cursor will be invisible, too. It will remain invisible until you invoke the [`unhide()`](nscursor/unhide().md) method.

Each invocation of `hide` must be balanced by an invocation of [`unhide()`](nscursor/unhide().md) in order for the cursor to be displayed.

The [`hide()`](nscursor/hide().md) method overrides [`setHiddenUntilMouseMoves(_:)`](nscursor/sethiddenuntilmousemoves(_:).md).

## See Also

- [var image: UIImage](nscursor/image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](nscursor/hotspot.md)
  The position of the click location within the cursor.
- [class func unhide()](nscursor/unhide.md)
  Negates an earlier call to [`hide()`](nscursor/hide().md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](nscursor/sethiddenuntilmousemoves(_:).md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/hide())*