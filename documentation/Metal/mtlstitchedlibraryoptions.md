# MTLStitchedLibraryOptions

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct MTLStitchedLibraryOptions
```

```c
enum MTLStitchedLibraryOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./mtlstitchedlibraryoptions/init%28rawvalue%29.md)
### Type Properties
- [static var failOnBinaryArchiveMiss: MTLStitchedLibraryOptions](./mtlstitchedlibraryoptions/failonbinaryarchivemiss.md)
  An option that instructs the compiler to return an error when a GPU function for a stitched library isn’t in a binary archive.
- [static var storeLibraryInMetalPipelinesScript: MTLStitchedLibraryOptions](./mtlstitchedlibraryoptions/storelibraryinmetalpipelinesscript.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Structures
- [struct MTLTensorError](./mtltensorerror-swift.struct.md)
- [struct MTLBinaryArchiveError](./mtlbinaryarchiveerror-swift.struct.md)
  An error that occurred when creating a binary shader archive.
- [struct MTLCommandBufferError](./mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [struct MTLComponentTransform](./mtlcomponenttransform.md)
- [struct MTLCounterSampleBufferError](./mtlcountersamplebuffererror-swift.struct.md)
  The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [struct MTLDynamicLibraryError](./mtldynamiclibraryerror-swift.struct.md)
  Errors when compiling dynamic libraries.
- [struct MTLIOError](./mtlioerror-swift.struct.md)
  The categories of errors for creating an input/output file handle.
- [struct MTLPackedFloatQuaternion](./mtlpackedfloatquaternion.md)
- [struct NSDeviceCertification](./nsdevicecertification.md)
- [struct NSProcessPerformanceProfile](./nsprocessperformanceprofile.md)
  A value describing the device’s performance profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstitchedlibraryoptions)*