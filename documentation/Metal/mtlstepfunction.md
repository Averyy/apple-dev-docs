# MTLStepFunction

**Framework**: Metal  
**Kind**: enum

The frequency and locations at which a function fetches attribute data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLStepFunction
```

## Topics

### Step options
- [MTLStepFunction.constant](mtlstepfunction/constant.md)
  The function fetches attribute data once.
- [MTLStepFunction.perInstance](mtlstepfunction/perinstance.md)
  The function fetches data based on the instance index.
- [MTLStepFunction.perPatch](mtlstepfunction/perpatch.md)
  The post-tessellation function fetches data based on the patch index of the patch.
- [MTLStepFunction.perPatchControlPoint](mtlstepfunction/perpatchcontrolpoint.md)
  The post-tessellation function fetches data based on the control-point indices associated with the patch.
- [MTLStepFunction.perVertex](mtlstepfunction/pervertex.md)
  The vertex function fetches data for every vertex.
- [MTLStepFunction.threadPositionInGridX](mtlstepfunction/threadpositioningridx.md)
  The compute function fetches data based on the thread’s `x` coordinate.
- [MTLStepFunction.threadPositionInGridY](mtlstepfunction/threadpositioningridy.md)
  The compute function fetches data based on the thread’s `y` coordinate.
- [MTLStepFunction.threadPositionInGridXIndexed](mtlstepfunction/threadpositioningridxindexed.md)
  The compute function fetches data by using the thread’s `x` coordinate to look up a value in the index buffer.
- [MTLStepFunction.threadPositionInGridYIndexed](mtlstepfunction/threadpositioningridyindexed.md)
  The compute function fetches data by using the thread’s `y` coordinate to look up a value in the index buffer.
### Initializers
- [init?(rawValue: UInt)](mtlstepfunction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var stride: Int](mtlbufferlayoutdescriptor/stride.md)
  The number of bytes from one buffer entry to the next.
- [var stepFunction: MTLStepFunction](mtlbufferlayoutdescriptor/stepfunction.md)
  Determines how and when compute functions fetch data.
- [var stepRate: Int](mtlbufferlayoutdescriptor/steprate.md)
  How frequently the step function should load data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstepfunction)*