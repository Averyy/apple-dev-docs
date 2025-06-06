# patternInput

**Framework**: Game Controller  
**Kind**: property

The input object for a pattern gear shift.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var patternInput: (any GCSwitchPositionInput)? { get }
```

#### Discussion

If this property is `nil`, the gear shift isn’t a pattern gear shift. A pattern gear shift lays out the gears in a pattern that lets the user move to any gear. If the [`position`](gcswitchpositioninput/position.md) property of this property is `0`, the gear shift is in neutral. If it’s `-1`, the gear shift is in reverse.

## See Also

- [var sequentialInput: (any GCRelativeInput)?](gcgearshifterelement/sequentialinput.md)
  The input object for a sequential gear shift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgearshifterelement/patterninput)*