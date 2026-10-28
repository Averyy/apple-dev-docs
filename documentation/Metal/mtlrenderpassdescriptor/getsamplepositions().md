# getSamplePositions()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Returns the programmable sample positions set for a render pass.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS

## Declaration

```swift
func getSamplePositions() -> [MTLSamplePosition]
```

## Return Value

An array of programmable sample positions.

## See Also

### Using programmable sample positions
- [func MTLSamplePositionMake(Float, Float) -> MTLSamplePosition](../mtlsamplepositionmake%28_,_%29.md)
  Returns a new sample position on a subpixel grid.
- [func setSamplePositions([MTLSamplePosition])](./setsamplepositions%28_%29.md)
  Sets the programmable sample positions for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/getsamplepositions())*