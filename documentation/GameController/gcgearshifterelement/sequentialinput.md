# sequentialInput

**Framework**: Game Controller  
**Kind**: property

The input object for a sequential gear shift.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var sequentialInput: (any GCRelativeInput)? { get }
```

#### Discussion

If this property is `nil`, this gear shift isn’t a sequential gear shift. A sequential gear shift requires the user to move through the gears in sequence.

## See Also

- [var patternInput: (any GCSwitchPositionInput)?](gcgearshifterelement/patterninput.md)
  The input object for a pattern gear shift.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgearshifterelement/sequentialinput)*