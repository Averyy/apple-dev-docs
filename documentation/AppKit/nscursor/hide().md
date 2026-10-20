# hide()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) hide;
```

#### Discussion

If another cursor becomes current, that cursor will be invisible, too. It will remain invisible until you invoke the [`unhide()`](./unhide%28%29.md) method.

Each invocation of `hide` must be balanced by an invocation of [`unhide()`](./unhide%28%29.md) in order for the cursor to be displayed.

The [`hide()`](./hide%28%29.md) method overrides [`setHiddenUntilMouseMoves(_:)`](./sethiddenuntilmousemoves%28_%29.md).

## See Also

### Setting cursor attributes
- [var image: UIImage](./image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](./hotspot.md)
  The position of the click location within the cursor.
- [class func unhide()](./unhide%28%29.md)
  Negates an earlier call to [`hide()`](./hide%28%29.md) by showing the current cursor.
- [class func setHiddenUntilMouseMoves(Bool)](./sethiddenuntilmousemoves%28_%29.md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/hide())*