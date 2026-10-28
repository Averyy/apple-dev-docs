# activate()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Activates the receiver.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func activate()
```

```objc
- (void) activate;
```

## Discussion

You should not call this method directly; it is invoked by the system. It is provided as an override point for subclasses.

## See Also

### Activating the Input Context
- [func deactivate()](./deactivate%28%29.md)
  Deactivates the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/activate())*