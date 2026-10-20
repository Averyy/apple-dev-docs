# makeTouchBar()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Your custom subclass of the `NSResponder` class should override this method to create and configure your subclass’s default [`NSTouchBar`](../nstouchbar.md) object.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func makeTouchBar() -> NSTouchBar?
```

```objc
- (NSTouchBar *) makeTouchBar;
```

## See Also

### Supporting the Touch Bar
- [var touchBar: NSTouchBar?](./touchbar.md)
  The [`NSTouchBar`](../nstouchbar.md) object associated with the responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/maketouchbar())*