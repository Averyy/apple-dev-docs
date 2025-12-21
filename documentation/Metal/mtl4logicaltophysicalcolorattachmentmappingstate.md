# MTL4LogicalToPhysicalColorAttachmentMappingState

**Framework**: Metal  
**Kind**: enum

Enumerates possible behaviors of how a pipeline maps its logical outputs to its color attachments.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MTL4LogicalToPhysicalColorAttachmentMappingState
```

## Topics

### Enumeration Cases
- [MTL4LogicalToPhysicalColorAttachmentMappingState.identity](mtl4logicaltophysicalcolorattachmentmappingstate/identity.md)
  Treats the logical color attachment descriptor array for render and tile render pipelines to match the physical one.
- [MTL4LogicalToPhysicalColorAttachmentMappingState.inherited](mtl4logicaltophysicalcolorattachmentmappingstate/inherited.md)
  Deduces the color attachment mapping by inheriting it from the color attachment map of the current encoder.
### Initializers
- [init?(rawValue: Int)](mtl4logicaltophysicalcolorattachmentmappingstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum MTL4BlendState](mtl4blendstate.md)
  Enumeration for controlling the blend state of a pipeline state object.
- [class MTL4FunctionDescriptor](mtl4functiondescriptor.md)
  Base interface for describing a Metal 4 shader function.
- [enum MTL4IndirectCommandBufferSupportState](mtl4indirectcommandbuffersupportstate.md)
  Enumeration for controlling support for [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md).
- [class MTL4LibraryDescriptor](mtl4librarydescriptor.md)
  Serves as the base descriptor for creating a Metal library.
- [class MTL4LibraryFunctionDescriptor](mtl4libraryfunctiondescriptor.md)
  Describes a shader function from a Metal library.
- [typealias MTL4NewBinaryFunctionCompletionHandler](mtl4newbinaryfunctioncompletionhandler.md)
  Provides a signature for a callback block that Metal calls when the compiler finishes a build task for a binary function.
- [typealias MTL4NewMachineLearningPipelineStateCompletionHandler](mtl4newmachinelearningpipelinestatecompletionhandler.md)
  Provides a signature for a callback block that Metal calls when the compiler finishes a build task for a machine learning pipeline state.
- [struct MTL4ShaderReflection](mtl4shaderreflection.md)
  Option mask for requesting reflection information at pipeline build time.
- [class MTL4SpecializedFunctionDescriptor](mtl4specializedfunctiondescriptor.md)
  Groups together properties to configure and create a specialized function by passing it to a factory method.
- [enum MTL4AlphaToCoverageState](mtl4alphatocoveragestate.md)
  Enumeration for controlling alpha-to-coverage state of a pipeline state object.
- [enum MTL4AlphaToOneState](mtl4alphatoonestate.md)
  Enumeration for controlling alpha-to-one state of a pipeline state object.
- [class MTL4StaticLinkingDescriptor](mtl4staticlinkingdescriptor.md)
  Groups together properties to drive a static linking process.
- [class MTL4StitchedFunctionDescriptor](mtl4stitchedfunctiondescriptor.md)
  Groups together properties that describe a shader function suitable for stitching.
- [class MTLFunctionReflection](mtlfunctionreflection.md)
  Represents a reflection object containing information about a function in a Metal library.
- [typealias MTLNewDynamicLibraryCompletionHandler](mtlnewdynamiclibrarycompletionhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4logicaltophysicalcolorattachmentmappingstate)*