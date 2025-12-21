# stages()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Queries a bitmask representing the shader stages on which commands currently present in this command encoder operate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func stages() -> MTLStages
```

#### Return Value

A bitmask representing shader stages that commands currently present in this command encoder operate on.

#### Discussion

Metal dynamically updates this property based on the commands you encode into the command encoder, for example, it sets the bit [`dispatch`](mtlstages/dispatch.md) if this encoder contains any commands that dispatch a compute kernel.

Similarly, it sets the bit [`blit`](mtlstages/blit.md) if this encoder contains any commands to copy or modify buffers, textures, or indirect command buffers.

Finally, Metal sets the bit [`accelerationStructure`](mtlstages/accelerationstructure.md) if this encoder contains any commands that build, copy, or refit acceleration structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/stages())*