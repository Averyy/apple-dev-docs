# isSetOnMouseExited

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isSetOnMouseExited: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver becomes current when it receives a [`mouseExited(with:)`](nscursor/mouseexited(with:).md) message; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

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
- [func setOnMouseExited(Bool)](nscursor/setonmouseexited(_:).md)
  Sets whether the receiver accepts [`mouseExited(with:)`](nscursor/mouseexited(with:).md) events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/issetonmouseexited)*