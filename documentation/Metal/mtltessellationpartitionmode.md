# MTLTessellationPartitionMode

**Framework**: Metal  
**Kind**: enum

Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLTessellationPartitionMode
```

#### Overview

The table lists the tessellation factor range for each partitioning mode.

| Partitioning mode | Tessellation factor range |
| --- | --- |
| [`MTLTessellationPartitionMode.pow2`](mtltessellationpartitionmode/pow2.md) | [`1`, [`maxTessellationFactor`](mtlrenderpipelinedescriptor/maxtessellationfactor.md)] |
| [`MTLTessellationPartitionMode.integer`](mtltessellationpartitionmode/integer.md) | [`1`, [`maxTessellationFactor`](mtlrenderpipelinedescriptor/maxtessellationfactor.md)] |
| [`MTLTessellationPartitionMode.fractionalOdd`](mtltessellationpartitionmode/fractionalodd.md) | [`1`, [`maxTessellationFactor`](mtlrenderpipelinedescriptor/maxtessellationfactor.md)-1] |
| [`MTLTessellationPartitionMode.fractionalEven`](mtltessellationpartitionmode/fractionaleven.md) | [`2`, [`maxTessellationFactor`](mtlrenderpipelinedescriptor/maxtessellationfactor.md)] |

The floating-point tessellation level is always clamped to its corresponding range before calculating the final tessellation factor. After clamping, the calculation depends on the chosen partitioning mode:

- For the [`MTLTessellationPartitionMode.pow2`](mtltessellationpartitionmode/pow2.md) partitioning mode, the result is rounded up to the nearest integer `n`, where `n` is a power of two. The corresponding edge is divided into `n` segments of equal length in (u, v) space.
- For the [`MTLTessellationPartitionMode.integer`](mtltessellationpartitionmode/integer.md) partitioning mode, the result is rounded up to the nearest integer `n`. The corresponding edge is divided into `n` segments of equal length in (u, v) space.
- For the [`MTLTessellationPartitionMode.fractionalOdd`](mtltessellationpartitionmode/fractionalodd.md) partitioning mode, the tessellation level is rounded up the the nearest odd integer `n`. If `n` is `1`, the edge is not subdivided. Otherwise, the corresponding edge is divided into `n-2` segments of equal length, and two additional segments of equal length that are typically shorter than the other segments. The length of the two additional segments relative to the others decreases monotonically by the value of `n-f`, where `f` is the clamped floating-point tessellation level. If `n-f` is `0` the additional segments equal length to the other segments. As `n-f` approaches `2`, the relative length of the additional segments approaches `0`. The two additional segments should be placed symmetrically on opposite sides of the subdivided edge. The relative location of these two segments is undefined, but needs to be identical for any pair of subdivided edges with identical values of `f`.
- For the [`MTLTessellationPartitionMode.fractionalEven`](mtltessellationpartitionmode/fractionaleven.md) partitioning mode, the tessellation level is rounded up the the nearest even integer `n`.

## Topics

### Partition modes
- [MTLTessellationPartitionMode.pow2](mtltessellationpartitionmode/pow2.md)
  A power of two partitioning mode.
- [MTLTessellationPartitionMode.integer](mtltessellationpartitionmode/integer.md)
  An integer partitioning mode.
- [MTLTessellationPartitionMode.fractionalOdd](mtltessellationpartitionmode/fractionalodd.md)
  A fractional odd partitioning mode.
- [MTLTessellationPartitionMode.fractionalEven](mtltessellationpartitionmode/fractionaleven.md)
  A fractional even partitioning mode.
### Initializers
- [init?(rawValue: UInt)](mtltessellationpartitionmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode)*