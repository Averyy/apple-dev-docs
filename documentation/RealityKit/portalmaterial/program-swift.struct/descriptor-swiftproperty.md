# descriptor

**Framework**: RealityKit  
**Kind**: property

The descriptor that produced this program.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var descriptor: PortalMaterial.Program.Descriptor { get }
```

#### Discussion

Use this property to inspect the shader graph and the input or function-constant values that were used to compile the program — for example, to enumerate the input names a parent material can set, or to construct a fresh descriptor with adjusted constants and recompile.

## See Also

- [PortalMaterial.Program.Descriptor](portalmaterial/program-swift.struct/descriptor-swift.struct.md)
  Configuration used to compile a [`PortalMaterial.Program`](portalmaterial/program-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.property)*