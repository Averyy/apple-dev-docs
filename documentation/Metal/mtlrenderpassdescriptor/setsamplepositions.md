# setSamplePositions(_:)

**Framework**: Metal  
**Kind**: method

Sets the programmable sample positions for a render pass.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func setSamplePositions(_ positions: [MTLSamplePosition])
```

#### Discussion

Programmable sample positions must be floating-point values in the `[0.0, 1.0)` range along each axis, with the origin `(0,0)` defined at the top-left corner. Values can be set from `0/16` up to `15/16`, inclusive, in `1/16` increments along each axis.

If the length of the array is `0`, the GPU uses the default sample positions for the render pass.

> **Note**:  Call the [`supportsTextureSampleCount(_:)`](mtldevice/supportstexturesamplecount(_:).md) method to determine whether the device object supports a specific sample count.

## Parameters

- `positions`: An array of programmable sample positions for the render pass. The number of programmable sample positions must match the render pass sample count you must specify an empty array.

## See Also

- [func MTLSamplePositionMake(Float, Float) -> MTLSamplePosition](mtlsamplepositionmake(_:_:).md)
  Returns a new sample position on a subpixel grid.
- [func getSamplePositions() -> [MTLSamplePosition]](mtlrenderpassdescriptor/getsamplepositions.md)
  Returns the programmable sample positions set for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/setsamplepositions(_:))*