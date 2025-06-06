# getSamplePositions()

**Framework**: Metal  
**Kind**: method

Returns the programmable sample positions set for a render pass.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func getSamplePositions() -> [MTLSamplePosition]
```

#### Return Value

An array of programmable sample positions.

## See Also

- [func MTLSamplePositionMake(Float, Float) -> MTLSamplePosition](mtlsamplepositionmake(_:_:).md)
  Returns a new sample position on a subpixel grid.
- [func setSamplePositions([MTLSamplePosition])](mtlrenderpassdescriptor/setsamplepositions(_:).md)
  Sets the programmable sample positions for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/getsamplepositions())*