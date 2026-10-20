# MTLStepFunction.perPatch

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The post-tessellation function fetches data based on the patch index of the patch.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case perPatch
```

```c
MTLStepFunctionPerPatch
```

## See Also

### Step options
- [MTLStepFunction.constant](./constant.md)
  The function fetches attribute data once.
- [MTLStepFunction.perInstance](./perinstance.md)
  The function fetches data based on the instance index.
- [MTLStepFunction.perPatchControlPoint](./perpatchcontrolpoint.md)
  The post-tessellation function fetches data based on the control-point indices associated with the patch.
- [MTLStepFunction.perVertex](./pervertex.md)
  The vertex function fetches data for every vertex.
- [MTLStepFunction.threadPositionInGridX](./threadpositioningridx.md)
  The compute function fetches data based on the thread’s `x` coordinate.
- [MTLStepFunction.threadPositionInGridY](./threadpositioningridy.md)
  The compute function fetches data based on the thread’s `y` coordinate.
- [MTLStepFunction.threadPositionInGridXIndexed](./threadpositioningridxindexed.md)
  The compute function fetches data by using the thread’s `x` coordinate to look up a value in the index buffer.
- [MTLStepFunction.threadPositionInGridYIndexed](./threadpositioningridyindexed.md)
  The compute function fetches data by using the thread’s `y` coordinate to look up a value in the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstepfunction/perpatch)*