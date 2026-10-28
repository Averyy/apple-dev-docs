# unhide()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Negates an earlier call to [`hide()`](./hide%28%29.md) by showing the current cursor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func unhide()
```

```objc
+ (void) unhide;
```

## Discussion

Each invocation of `unhide` must be balanced by an invocation of [`hide()`](./hide%28%29.md) in order for the cursor display to be correct.

## See Also

### Setting cursor attributes
- [var image: UIImage](./image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](./hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](./hide%28%29.md)
  Makes the current cursor invisible.
- [class func setHiddenUntilMouseMoves(Bool)](./sethiddenuntilmousemoves%28_%29.md)
  Sets whether the cursor is hidden until the mouse moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/unhide())*