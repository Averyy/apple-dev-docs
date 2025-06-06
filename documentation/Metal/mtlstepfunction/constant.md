# MTLStepFunction.constant

**Framework**: Metal  
**Kind**: case

The function fetches attribute data once.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case constant
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstepfunction/constant)*