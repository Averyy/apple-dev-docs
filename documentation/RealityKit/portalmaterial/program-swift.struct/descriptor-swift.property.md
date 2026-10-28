# descriptor

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The descriptor that produced this program.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var descriptor: PortalMaterial.Program.Descriptor { get }
```

## Discussion

Use this property to inspect the shader graph and the input or function-constant values that were used to compile the program — for example, to enumerate the input names a parent material can set, or to construct a fresh descriptor with adjusted constants and recompile.

## See Also

### Configuring the program
- [PortalMaterial.Program.Descriptor](./descriptor-swift.struct.md)
  Configuration used to compile a [`PortalMaterial.Program`](../program-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.property)*