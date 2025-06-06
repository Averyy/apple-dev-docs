# unhide(_:)

**Framework**: AppKit  
**Kind**: method

Restores hidden windows to the screen and makes the receiver active.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func unhide(_ sender: Any?)
```

#### Discussion

Invokes [`unhideWithoutActivation()`](nsapplication/unhidewithoutactivation().md).

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func activate(ignoringOtherApps: Bool)](nsapplication/activate(ignoringotherapps:).md)
  Makes the receiver the active app.
- [var isHidden: Bool](nsapplication/ishidden.md)
  A Boolean value indicating whether the app is hidden.
- [func hide(Any?)](nsapplication/hide(_:).md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhideWithoutActivation()](nsapplication/unhidewithoutactivation.md)
  Restores hidden windows without activating their owner (the receiver).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/unhide(_:))*