# tessellationOutputWindingOrder

**Framework**: Metal  
**Kind**: property

The winding order of triangles from the tessellator.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var tessellationOutputWindingOrder: MTLWinding { get set }
```

#### Discussion

The default value is [`MTLWinding.clockwise`](mtlwinding/clockwise.md).

## See Also

- [var maxTessellationFactor: Int](mtlrenderpipelinedescriptor/maxtessellationfactor.md)
  The maximum tessellation factor that the tessellator uses when tessellating patches.
- [var isTessellationFactorScaleEnabled: Bool](mtlrenderpipelinedescriptor/istessellationfactorscaleenabled.md)
  A Boolean value that determines whether the pipeline scales the tessellation factor.
- [var tessellationFactorFormat: MTLTessellationFactorFormat](mtlrenderpipelinedescriptor/tessellationfactorformat.md)
  The format of the tessellation factors in the tessellation factor buffer.
- [var tessellationControlPointIndexType: MTLTessellationControlPointIndexType](mtlrenderpipelinedescriptor/tessellationcontrolpointindextype.md)
  The size of the control point indices in a control point index buffer.
- [var tessellationFactorStepFunction: MTLTessellationFactorStepFunction](mtlrenderpipelinedescriptor/tessellationfactorstepfunction.md)
  The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [var tessellationPartitionMode: MTLTessellationPartitionMode](mtlrenderpipelinedescriptor/tessellationpartitionmode.md)
  The partitioning mode that the tessellator uses to derive the number and spacing of segments for subdividing a corresponding edge.
- [enum MTLTessellationFactorFormat](mtltessellationfactorformat.md)
  Options for specifying the format of the tessellation factors in a tessellation factor buffer.
- [enum MTLTessellationControlPointIndexType](mtltessellationcontrolpointindextype.md)
  Options for specifying the size of the control point indices in a control point index buffer.
- [enum MTLTessellationFactorStepFunction](mtltessellationfactorstepfunction.md)
  Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
- [enum MTLTessellationPartitionMode](mtltessellationpartitionmode.md)
  Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/tessellationoutputwindingorder)*