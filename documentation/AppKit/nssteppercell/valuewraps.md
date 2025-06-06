# valueWraps

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver wraps around the minimum and maximum values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var valueWraps: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if, when incrementing or decrementing, the value wraps around to the minimum or maximum. [`false`](https://developer.apple.com/documentation/swift/false) if the value stays pinned at the minimum or maximum. The default is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var autorepeat: Bool](nssteppercell/autorepeat.md)
  A Boolean value indicating how the receiver responds to mouse events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppercell/valuewraps)*