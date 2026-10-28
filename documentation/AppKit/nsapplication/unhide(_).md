# unhide(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Restores hidden windows to the screen and makes the receiver active.

**Availability**:
- macOS

## Declaration

```swift
func unhide(_ sender: Any?)
```

```objc
- (void) unhide:(id) sender;
```

## Discussion

Invokes [`unhideWithoutActivation()`](./unhidewithoutactivation%28%29.md).

## Parameters

- `sender`: The object that sent the command.

## See Also

### Related Documentation
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
### Hiding Windows
- [var isHidden: Bool](./ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func hide(Any?)](./hide%28_%29.md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhideWithoutActivation()](./unhidewithoutactivation%28%29.md)
  Restores hidden windows without activating their owner (the receiver).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unhide(_:))*