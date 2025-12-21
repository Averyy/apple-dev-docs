# ignoresMultiClick

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver ignores multiple clicks made in rapid succession.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var ignoresMultiClick: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver ignores multiple clicks; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

By default, controls treat double clicks as two distinct clicks, triple clicks as three distinct clicks, and so on. However, if you set this propery to [`true`](https://developer.apple.com/documentation/Swift/true), additional clicks (within a predetermined interval after the first) occurring after the first click are not processed by the receiver, and are instead passed on to `super`.

## See Also

- [func mouseDown(with: NSEvent)](nsresponder/mousedown(with:).md)
  Informs the receiver that the user has pressed the left mouse button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/ignoresmulticlick)*