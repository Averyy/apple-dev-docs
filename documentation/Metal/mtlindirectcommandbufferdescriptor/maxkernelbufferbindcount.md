# maxKernelBufferBindCount

**Framework**: Metal  
**Kind**: property

The maximum number of buffers that you can set per command for the compute kernel.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var maxKernelBufferBindCount: Int { get set }
```

#### Discussion

Metal ignores this property if [`inheritBuffers`](mtlindirectcommandbufferdescriptor/inheritbuffers.md) is [`true`](https://developer.apple.com/documentation/Swift/true) or if you configured [`commandTypes`](mtlindirectcommandbufferdescriptor/commandtypes.md) for rendering commands. Metal needs to reserve enough memory in each command to store this many arguments. Use the smallest value that works for all commands you plan to encode into the indirect command buffer.

## See Also

- [var maxVertexBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount.md)
  The maximum number of buffers that you can set per command for the vertex stage.
- [var maxFragmentBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxfragmentbufferbindcount.md)
  The maximum number of buffers that you can set per command for the fragment stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount)*