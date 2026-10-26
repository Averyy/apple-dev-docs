# MTLSamplePositionMake(_:_:)

**Framework**: Metal  
**Kind**: func  
**Role**: Function

Returns a new sample position on a subpixel grid.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MTLSamplePositionMake(_ x: Float, _ y: Float) -> MTLSamplePosition
```

```c
static MTLSamplePosition MTLSamplePositionMake(float x, float y);
```

#### Return Value

The new sample position.

## Parameters

- `x`: The x coordinate.
- `y`: The y coordinate.

## See Also

### Using programmable sample positions
- [func setSamplePositions([MTLSamplePosition])](./mtlrenderpassdescriptor/setsamplepositions%28_%29.md)
  Sets the programmable sample positions for a render pass.
- [func getSamplePositions() -> [MTLSamplePosition]](./mtlrenderpassdescriptor/getsamplepositions%28%29.md)
  Returns the programmable sample positions set for a render pass.
- [- setSamplePositions:count:](./mtlrenderpassdescriptor/setsamplepositions_count_.md)
  Sets the programmable sample positions for a render pass.
- [- getSamplePositions:count:](./mtlrenderpassdescriptor/getsamplepositions_count_.md)
  Retrieves the programmable sample positions set for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplepositionmake(_:_:))*