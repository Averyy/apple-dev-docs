# stepFunction

**Framework**: Metal  
**Kind**: property

The circumstances under which the vertex and its attributes are presented to the vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var stepFunction: MTLVertexStepFunction { get set }
```

#### Discussion

The default value is [`MTLVertexStepFunction.perVertex`](mtlvertexstepfunction/pervertex.md).

If `stepFunction` is [`MTLVertexStepFunction.perVertex`](mtlvertexstepfunction/pervertex.md), the function fetches new attribute data based on the `[[ vertex_id ]]` attribute qualifier. The function fetches new attribute data each time a new vertex is processed. In this case, `stepRate` must be set to `1`, which is its default value.

If `stepFunction` is [`MTLVertexStepFunction.perInstance`](mtlvertexstepfunction/perinstance.md), the function fetches new attribute data based on the `[[ instance_id ]]` attribute qualifier.  In this case, `stepRate` must be greater than `0` and its value determines how often the function fetches new attribute data.

If `stepFunction` is [`MTLVertexStepFunction.constant`](mtlvertexstepfunction/constant.md), the function fetches attribute data just once, and that attribute data is used for every vertex. In this case,`stepRate` must be set to `0`.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [var stepRate: Int](mtlvertexbufferlayoutdescriptor/steprate.md)
  The interval at which the vertex and its attributes are presented to the vertex function.
- [var stride: Int](mtlvertexbufferlayoutdescriptor/stride.md)
  The number of bytes between the first byte of two consecutive vertices in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/stepfunction)*