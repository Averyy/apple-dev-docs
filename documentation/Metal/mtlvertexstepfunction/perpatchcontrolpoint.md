# MTLVertexStepFunction.perPatchControlPoint

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The post-tessellation vertex function fetches data based on the control-point indices associated with the patch.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case perPatchControlPoint
```

```c
MTLVertexStepFunctionPerPatchControlPoint
```

## See Also

### Step functions
- [MTLVertexStepFunction.constant](./constant.md)
  The vertex function fetches attribute data once and uses that data for every vertex.
- [MTLVertexStepFunction.perVertex](./pervertex.md)
  The vertex function fetches and uses new attribute data for every vertex.
- [MTLVertexStepFunction.perInstance](./perinstance.md)
  The vertex function regularly fetches new attribute data for a number of instances that is determined by `stepRate`.
- [MTLVertexStepFunction.perPatch](./perpatch.md)
  The post-tessellation vertex function fetches data based on the patch index of the patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perpatchcontrolpoint)*