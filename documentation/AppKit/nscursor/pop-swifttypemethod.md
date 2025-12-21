# pop()

**Framework**: AppKit  
**Kind**: method

Pops the current cursor off the top of the stack.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class func pop()
```

#### Discussion

The new object on the top of the stack becomes the current cursor. If the current cursor is the only cursor on the stack, this method does nothing.

## See Also

- [func pop()](nscursor/pop-swift.method.md)
  Sends a [`pop()`](nscursor/pop()-swift.type.method.md) message to the receiver’s class.
- [func push()](nscursor/push.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](nscursor/set.md)
  Makes the receiver the current cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/pop()-swift.type.method)*