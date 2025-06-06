# autorepeat

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating how the receiver responds to mouse events.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autorepeat: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the first mouse down will do one increment (decrement), and, after a delay of 0.5 seconds, will increment (decrement) at a rate of ten times per second. If [`false`](https://developer.apple.com/documentation/swift/false), the receiver will do one increment (decrement) on a mouse up. The default is [`true`](https://developer.apple.com/documentation/swift/true)

## See Also

- [var valueWraps: Bool](nssteppercell/valuewraps.md)
  A Boolean value indicating whether the receiver wraps around the minimum and maximum values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppercell/autorepeat)*