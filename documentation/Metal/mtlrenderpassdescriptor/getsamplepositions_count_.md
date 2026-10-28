# getSamplePositions:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Retrieves the programmable sample positions set for a render pass.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (NSUInteger) getSamplePositions:(MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Return Value

The total number of programmable sample positions set for the render pass.

## Discussion

The value of `count` needs to be equal to the number of programmable sample positions set by a previous call to the [`setSamplePositions:count:`](./setsamplepositions_count_.md) method (the `count` parameter). Also, the `positions` array needs to contain at least as many elements as the value of `count`.

If you don’t know the correct value for `count`, you may query this method by passing a `nil` array for `positions` and a `0` value for `count`. This method returns the number of programmable sample positions that are currently set.

## Parameters

- `positions`: A pointer to a destination array of sample positions where Metal writes the programmable sample positions.
- `count`: The number of programmable sample positions to retrieve.

## See Also

### Using programmable sample positions
- [func MTLSamplePositionMake(Float, Float) -> MTLSamplePosition](../mtlsamplepositionmake%28_,_%29.md)
  Returns a new sample position on a subpixel grid.
- [- setSamplePositions:count:](./setsamplepositions_count_.md)
  Sets the programmable sample positions for a render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/getsamplepositions:count:)*