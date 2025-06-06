# minValue

**Framework**: AppKit  
**Kind**: property

The minimum value the slider can send to its target.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var minValue: Double { get set }
```

#### Discussion

A vertical slider sends this value when its knob is at the bottom; a horizontal slider sends it when its knob is all the way to the left; a circular slider sends it when its knob is at the top.

## See Also

- [var maxValue: Double](nsslidercell/maxvalue.md)
  The maximum value the slider can send to its target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/minvalue)*