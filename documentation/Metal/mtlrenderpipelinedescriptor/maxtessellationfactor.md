# maxTessellationFactor

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The maximum tessellation factor that the tessellator uses when tessellating patches.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var maxTessellationFactor: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger maxTessellationFactor;
```

#### Discussion

The default value is `16` and the maximum value is `64`. Any value in between needs to be set according to the partitioning mode specified by the [`tessellationPartitionMode`](./tessellationpartitionmode.md) property:

- For the [`MTLTessellationPartitionMode.pow2`](../mtltessellationpartitionmode/pow2.md) partitioning mode, the value needs to be a power of two.
- For the [`MTLTessellationPartitionMode.integer`](../mtltessellationpartitionmode/integer.md) partitioning mode, the value can be an even or odd number.
- For the [`MTLTessellationPartitionMode.fractionalOdd`](../mtltessellationpartitionmode/fractionalodd.md) or [`MTLTessellationPartitionMode.fractionalEven`](../mtltessellationpartitionmode/fractionaleven.md) partitioning mode, the value needs to be an even number.

## See Also

### Specifying tessellation state
- [var isTessellationFactorScaleEnabled: Bool](./istessellationfactorscaleenabled.md)
  A Boolean value that determines whether the pipeline scales the tessellation factor.
- [var tessellationFactorFormat: MTLTessellationFactorFormat](./tessellationfactorformat.md)
  The format of the tessellation factors in the tessellation factor buffer.
- [var tessellationControlPointIndexType: MTLTessellationControlPointIndexType](./tessellationcontrolpointindextype.md)
  The size of the control point indices in a control point index buffer.
- [var tessellationFactorStepFunction: MTLTessellationFactorStepFunction](./tessellationfactorstepfunction.md)
  The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [var tessellationOutputWindingOrder: MTLWinding](./tessellationoutputwindingorder.md)
  The winding order of triangles from the tessellator.
- [var tessellationPartitionMode: MTLTessellationPartitionMode](./tessellationpartitionmode.md)
  The partitioning mode that the tessellator uses to derive the number and spacing of segments for subdividing a corresponding edge.
- [enum MTLTessellationFactorFormat](../mtltessellationfactorformat.md)
  Options for specifying the format of the tessellation factors in a tessellation factor buffer.
- [enum MTLTessellationControlPointIndexType](../mtltessellationcontrolpointindextype.md)
  Options for specifying the size of the control point indices in a control point index buffer.
- [enum MTLTessellationFactorStepFunction](../mtltessellationfactorstepfunction.md)
  Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
- [enum MTLTessellationPartitionMode](../mtltessellationpartitionmode.md)
  Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/maxtessellationfactor)*