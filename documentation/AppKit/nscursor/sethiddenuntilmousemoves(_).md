# setHiddenUntilMouseMoves(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) setHiddenUntilMouseMoves:(BOOL) flag;
```

#### Discussion

Do not try to counter this method by invoking [`unhide()`](./unhide%28%29.md). The results are undefined.

## Parameters

- `flag`: [`true`](../../Swift/true.md) to hide the cursor until one of the following occurs:

  - The mouse moves.
  - You invoke the method again, with `flag` set to [`false`](../../Swift/false.md).

## See Also

### Setting cursor attributes
- [var image: UIImage](./image.md)
  The cursor’s image.
- [var hotSpot: NSPoint](./hotspot.md)
  The position of the click location within the cursor.
- [class func hide()](./hide%28%29.md)
  Makes the current cursor invisible.
- [class func unhide()](./unhide%28%29.md)
  Negates an earlier call to [`hide()`](./hide%28%29.md) by showing the current cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/sethiddenuntilmousemoves(_:))*