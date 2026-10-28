# isTessellationFactorScaleEnabled

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite, getter=isTessellationFactorScaleEnabled) BOOL tessellationFactorScaleEnabled;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

If this value is [`true`](../../Swift/true.md), a scale factor is applied to the tessellation factors after the patch cull check is performed but before the tessellation factors are clamped to the value of [`maxTessellationFactor`](./maxtessellationfactor.md). The scale factor is applied only if the patch is not culled.

## See Also

### Related Documentation
- [func setTessellationFactorScale(Float)](../mtlrendercommandencoder/settessellationfactorscale%28_%29.md)
  Configures the scale factor for per-patch tessellation factors.
### Specifying tessellation state
- [var maxTessellationFactor: Int](./maxtessellationfactor.md)
  The maximum tessellation factor that the tessellator uses when tessellating patches.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/istessellationfactorscaleenabled)*