# maxValue

**Framework**: AppKit  
**Kind**: property

The maximum value the slider can send to its target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var maxValue: Double { get set }
```

#### Discussion

The slider’s maximum value. A horizontal slider sends the maximum value when the knob is all the way to the trailing end of the bar. A vertical slider sends the maximum value when the knob is at the top.

## See Also

- [var minValue: Double](nsslider/minvalue.md)
  The minimum value the slider can send to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/maxvalue)*