# isTessellationFactorScaleEnabled

**Framework**: Metal  
**Kind**: property

A Boolean value that determines whether the pipeline scales the tessellation factor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isTessellationFactorScaleEnabled: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

If this value is [`true`](https://developer.apple.com/documentation/swift/true), a scale factor is applied to the tessellation factors after the patch cull check is performed but before the tessellation factors are clamped to the value of [`maxTessellationFactor`](mtlrenderpipelinedescriptor/maxtessellationfactor.md). The scale factor is applied only if the patch is not culled.

## See Also

- [func setTessellationFactorScale(Float)](mtlrendercommandencoder/settessellationfactorscale(_:).md)
  Configures the scale factor for per-patch tessellation factors.
- [var maxTessellationFactor: Int](mtlrenderpipelinedescriptor/maxtessellationfactor.md)
  The maximum tessellation factor that the tessellator uses when tessellating patches.
- [var tessellationFactorFormat: MTLTessellationFactorFormat](mtlrenderpipelinedescriptor/tessellationfactorformat.md)
  The format of the tessellation factors in the tessellation factor buffer.
- [var tessellationControlPointIndexType: MTLTessellationControlPointIndexType](mtlrenderpipelinedescriptor/tessellationcontrolpointindextype.md)
  The size of the control point indices in a control point index buffer.
- [var tessellationFactorStepFunction: MTLTessellationFactorStepFunction](mtlrenderpipelinedescriptor/tessellationfactorstepfunction.md)
  The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [var tessellationOutputWindingOrder: MTLWinding](mtlrenderpipelinedescriptor/tessellationoutputwindingorder.md)
  The winding order of triangles from the tessellator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/istessellationfactorscaleenabled)*