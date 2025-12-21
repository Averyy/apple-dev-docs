# valueWraps

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the stepper wraps around the minimum and maximum values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var valueWraps: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if, when incrementing or decrementing, the value wraps around to the minimum or maximum. [`false`](https://developer.apple.com/documentation/Swift/false) if the value stays pinned at the minimum or maximum. The default is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var autorepeat: Bool](nsstepper/autorepeat.md)
  A Boolean value that indicates how the stepper responds to mouse events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstepper/valuewraps)*