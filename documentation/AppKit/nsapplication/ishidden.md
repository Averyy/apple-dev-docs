# isHidden

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the app is hidden.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isHidden: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the app is hidden or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

## See Also

- [func hide(Any?)](nsapplication/hide(_:).md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhide(Any?)](nsapplication/unhide(_:).md)
  Restores hidden windows to the screen and makes the receiver active.
- [func unhideWithoutActivation()](nsapplication/unhidewithoutactivation.md)
  Restores hidden windows without activating their owner (the receiver).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/ishidden)*