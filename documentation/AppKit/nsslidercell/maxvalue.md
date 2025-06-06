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

A horizontal slider sends its maximum value when the knob is at the right end of the slider; a vertical slider sends it when the knob is at the top. The maximum selectable value for a circular slider is just below [`maxValue`](nsslidercell/maxvalue.md); for example, if [`maxValue`](nsslidercell/maxvalue.md) is 360, you can set the dial up to 359.999.

## See Also

- [var minValue: Double](nsslidercell/minvalue.md)
  The minimum value the slider can send to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/maxvalue)*