# maxVertexBufferBindCount

**Framework**: Metal  
**Kind**: property

The maximum number of buffers that you can set per command for the vertex stage.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var maxVertexBufferBindCount: Int { get set }
```

#### Discussion

Metal ignores this property if [`inheritBuffers`](mtlindirectcommandbufferdescriptor/inheritbuffers.md) is [`true`](https://developer.apple.com/documentation/swift/true) or if you configured [`commandTypes`](mtlindirectcommandbufferdescriptor/commandtypes.md) for compute commands. Metal must reserve enough memory in each command to store this many arguments. Use the smallest value that works for all commands you plan to encode into the indirect command buffer.

## See Also

- [var maxFragmentBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxfragmentbufferbindcount.md)
  The maximum number of buffers that you can set per command for the fragment stage.
- [var maxKernelBufferBindCount: Int](mtlindirectcommandbufferdescriptor/maxkernelbufferbindcount.md)
  The maximum number of buffers that you can set per command for the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount)*