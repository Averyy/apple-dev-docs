# valueWraps

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the stepper wraps around the minimum and maximum values.

**Availability**:
- macOS

## Declaration

```swift
var valueWraps: Bool { get set }
```

```objc
@property BOOL valueWraps;
```

## Discussion

[`true`](../../Swift/true.md) if, when incrementing or decrementing, the value wraps around to the minimum or maximum. [`false`](../../Swift/false.md) if the value stays pinned at the minimum or maximum. The default is [`true`](../../Swift/true.md).

## See Also

### Specifying how the stepper responds
- [var autorepeat: Bool](./autorepeat.md)
  A Boolean value that indicates how the stepper responds to mouse events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstepper/valuewraps)*