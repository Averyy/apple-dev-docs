# pop()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) pop;
```

#### Discussion

The new object on the top of the stack becomes the current cursor. If the current cursor is the only cursor on the stack, this method does nothing.

## See Also

### Controlling which cursor is current
- [func pop()](./pop%28%29-swift.method.md)
  Sends a [`pop()`](./pop%28%29-swift.type.method.md) message to the receiver’s class.
- [func push()](./push%28%29.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.
- [func set()](./set%28%29.md)
  Makes the receiver the current cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/pop()-swift.type.method)*