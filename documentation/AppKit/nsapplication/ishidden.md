# isHidden

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the app is hidden.

**Availability**:
- macOS

## Declaration

```swift
var isHidden: Bool { get }
```

```objc
@property (readonly, getter=isHidden) BOOL hidden;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the app is hidden or [`false`](../../Swift/false.md) if it is not.

## See Also

### Hiding Windows
- [func hide(Any?)](./hide%28_%29.md)
  Hides all the receiver’s windows, and the next app in line is activated.
- [func unhide(Any?)](./unhide%28_%29.md)
  Restores hidden windows to the screen and makes the receiver active.
- [func unhideWithoutActivation()](./unhidewithoutactivation%28%29.md)
  Restores hidden windows without activating their owner (the receiver).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/ishidden)*