# MTL4StitchedFunctionDescriptor

**Framework**: Metal  
**Kind**: class

Groups together properties that describe a shader function suitable for stitching.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4StitchedFunctionDescriptor
```

## Topics

### Instance Properties
- [var functionDescriptors: [MTL4FunctionDescriptor]?](mtl4stitchedfunctiondescriptor/functiondescriptors.md)
  Configures an array of function descriptors with references to functions that contribute to the stitching process.
- [var functionGraph: MTLFunctionStitchingGraph?](mtl4stitchedfunctiondescriptor/functiongraph.md)
  Sets the graph representing how to stitch functions together.

## Relationships

### Inherits From
- [MTL4FunctionDescriptor](mtl4functiondescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [class MTL4LinkedFunctions](mtl4linkedfunctions.md)
  Groups together functions to link.
- [enum MTL4LogicalToPhysicalColorAttachmentMappingState](mtl4logicaltophysicalcolorattachmentmappingstate.md)
  Enumerates possible behaviors of how a pipeline maps its logical outputs to its color attachments.
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
- [class MTLFunctionReflection](mtlfunctionreflection.md)
  Represents a reflection object containing information about a function in a Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4stitchedfunctiondescriptor)*