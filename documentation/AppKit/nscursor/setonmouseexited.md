# setOnMouseExited(_:)

**Framework**: AppKit  
**Kind**: method

Sets whether the receiver accepts [`mouseExited(with:)`](nscursor/mouseexited(with:).md) events.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setOnMouseExited(_ flag: Bool)
```

#### Discussion

Accepting [`mouseExited(with:)`](nscursor/mouseexited(with:).md) event messages allows the cursor to be made the current cursor when the cursor exits a view’s cursor rectangle.

## Parameters

- `flag`:   if the receiver accepts future   event messages; otherwise it ignores them.

## See Also

- [class func pop()](nscursor/pop-swift.type.method.md)
  Pops the current cursor off the top of the stack.
- [func pop()](nscursor/pop-swift.method.md)
  Sends a [`pop()`](nscursor/pop()-swift.type.method.md) message to the receiver’s class.
- [func push()](nscursor/push.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](nscursor/set.md)
  Makes the receiver the current cursor.
- [func mouseEntered(with: NSEvent)](nscursor/mouseentered(with:).md)
  Automatically sent to the receiver when the cursor enters a cursor rectangle owned by the receiver.
- [func setOnMouseEntered(Bool)](nscursor/setonmouseentered(_:).md)
  Specifies whether the receiver accepts [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) events.
- [var isSetOnMouseEntered: Bool](nscursor/issetonmouseentered.md)
  A Boolean value indicating whether the receiver becomes current on receiving a [`mouseEntered(with:)`](nscursor/mouseentered(with:).md) message.
- [func mouseExited(with: NSEvent)](nscursor/mouseexited(with:).md)
  Automatically sent to the receiver when the cursor exits a cursor rectangle owned by the receiver.
- [var isSetOnMouseExited: Bool](nscursor/issetonmouseexited.md)
  A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/setonmouseexited(_:))*