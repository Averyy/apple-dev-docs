# autorepeat

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating how the receiver responds to mouse events.

**Availability**:
- macOS

## Declaration

```swift
var autorepeat: Bool { get set }
```

```objc
@property BOOL autorepeat;
```

#### Discussion

If [`true`](../../Swift/true.md), the first mouse down will do one increment (decrement), and, after a delay of 0.5 seconds, will increment (decrement) at a rate of ten times per second. If [`false`](../../Swift/false.md), the receiver will do one increment (decrement) on a mouse up. The default is [`true`](../../Swift/true.md)

## See Also

### Specifying how stepper cell responds
- [var valueWraps: Bool](./valuewraps.md)
  A Boolean value indicating whether the receiver wraps around the minimum and maximum values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssteppercell/autorepeat)*