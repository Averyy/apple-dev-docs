# ignoresMultiClick

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver ignores multiple clicks made in rapid succession.

**Availability**:
- macOS

## Declaration

```swift
var ignoresMultiClick: Bool { get set }
```

```objc
@property BOOL ignoresMultiClick;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the receiver ignores multiple clicks; otherwise, [`false`](../../Swift/false.md).

By default, controls treat double clicks as two distinct clicks, triple clicks as three distinct clicks, and so on. However, if you set this propery to [`true`](../../Swift/true.md), additional clicks (within a predetermined interval after the first) occurring after the first click are not processed by the receiver, and are instead passed on to `super`.

## See Also

### Tracking the Mouse
- [func mouseDown(with: NSEvent)](../nsresponder/mousedown%28with%29.md)
  Informs the receiver that the user has pressed the left mouse button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/ignoresmulticlick)*