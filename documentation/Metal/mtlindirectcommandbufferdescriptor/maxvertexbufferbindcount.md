# maxVertexBufferBindCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) NSUInteger maxVertexBufferBindCount;
```

#### Discussion

Metal ignores this property if [`inheritBuffers`](./inheritbuffers.md) is [`true`](../../Swift/true.md) or if you configured [`commandTypes`](./commandtypes.md) for compute commands. Metal needs to reserve enough memory in each command to store this many arguments. Use the smallest value that works for all commands you plan to encode into the indirect command buffer.

## See Also

### Declaring the maximum number of argument buffers per command
- [var maxFragmentBufferBindCount: Int](./maxfragmentbufferbindcount.md)
  The maximum number of buffers that you can set per command for the fragment stage.
- [var maxKernelBufferBindCount: Int](./maxkernelbufferbindcount.md)
  The maximum number of buffers that you can set per command for the compute kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/maxvertexbufferbindcount)*