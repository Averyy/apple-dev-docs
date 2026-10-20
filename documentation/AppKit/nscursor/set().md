# set()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Makes the receiver the current cursor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
func set()
```

```objc
- (void) set;
```

## See Also

### Related Documentation
- [class var current: NSCursor](./current.md)
  Returns the application’s current cursor.
### Controlling which cursor is current
- [class func pop()](./pop%28%29-swift.type.method.md)
  Pops the current cursor off the top of the stack.
- [func pop()](./pop%28%29-swift.method.md)
  Sends a [`pop()`](./pop%28%29-swift.type.method.md) message to the receiver’s class.
- [func push()](./push%28%29.md)
  Puts the receiver on top of the cursor stack and makes it the current cursor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/set())*