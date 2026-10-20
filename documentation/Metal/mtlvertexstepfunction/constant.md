# MTLVertexStepFunction.constant

**Framework**: Metal  
**Kind**: case  
**Role**: Case

The vertex function fetches attribute data once and uses that data for every vertex.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
case constant
```

```c
MTLVertexStepFunctionConstant
```

## See Also

### Step functions
- [MTLVertexStepFunction.perVertex](./pervertex.md)
  The vertex function fetches and uses new attribute data for every vertex.
- [MTLVertexStepFunction.perInstance](./perinstance.md)
  The vertex function regularly fetches new attribute data for a number of instances that is determined by `stepRate`.
- [MTLVertexStepFunction.perPatch](./perpatch.md)
  The post-tessellation vertex function fetches data based on the patch index of the patch.
- [MTLVertexStepFunction.perPatchControlPoint](./perpatchcontrolpoint.md)
  The post-tessellation vertex function fetches data based on the control-point indices associated with the patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/constant)*