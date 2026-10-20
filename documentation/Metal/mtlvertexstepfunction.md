# MTLVertexStepFunction

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum MTLVertexStepFunction
```

```c
enum MTLVertexStepFunction : NSUInteger;
```

## Topics

### Step functions
- [MTLVertexStepFunction.constant](./mtlvertexstepfunction/constant.md)
  The vertex function fetches attribute data once and uses that data for every vertex.
- [MTLVertexStepFunction.perVertex](./mtlvertexstepfunction/pervertex.md)
  The vertex function fetches and uses new attribute data for every vertex.
- [MTLVertexStepFunction.perInstance](./mtlvertexstepfunction/perinstance.md)
  The vertex function regularly fetches new attribute data for a number of instances that is determined by `stepRate`.
- [MTLVertexStepFunction.perPatch](./mtlvertexstepfunction/perpatch.md)
  The post-tessellation vertex function fetches data based on the patch index of the patch.
- [MTLVertexStepFunction.perPatchControlPoint](./mtlvertexstepfunction/perpatchcontrolpoint.md)
  The post-tessellation vertex function fetches data based on the control-point indices associated with the patch.
### Initializers
- [init?(rawValue: UInt)](./mtlvertexstepfunction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Organizing the vertex buffer layout
- [var stepFunction: MTLVertexStepFunction](./mtlvertexbufferlayoutdescriptor/stepfunction.md)
  The circumstances under which the vertex and its attributes are presented to the vertex function.
- [var stepRate: Int](./mtlvertexbufferlayoutdescriptor/steprate.md)
  The interval at which the vertex and its attributes are presented to the vertex function.
- [var stride: Int](./mtlvertexbufferlayoutdescriptor/stride.md)
  The number of bytes between the first byte of two consecutive vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexstepfunction)*