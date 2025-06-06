# MTLComponentTransform

**Framework**: Metal  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLComponentTransform
```

## Topics

### Initializers
- [init()](mtlcomponenttransform/init.md)
- [init(scale: MTLPackedFloat3, shear: MTLPackedFloat3, pivot: MTLPackedFloat3, rotation: MTLPackedFloatQuaternion, translation: MTLPackedFloat3)](mtlcomponenttransform/init(scale:shear:pivot:rotation:translation:).md)
### Instance Properties
- [var pivot: MTLPackedFloat3](mtlcomponenttransform/pivot.md)
- [var rotation: MTLPackedFloatQuaternion](mtlcomponenttransform/rotation.md)
- [var scale: MTLPackedFloat3](mtlcomponenttransform/scale.md)
- [var shear: MTLPackedFloat3](mtlcomponenttransform/shear.md)
- [var translation: MTLPackedFloat3](mtlcomponenttransform/translation.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MTLBinaryArchiveError](mtlbinaryarchiveerror-swift.struct.md)
  An error that occurred when creating a binary shader archive.
- [struct MTLCommandBufferError](mtlcommandbuffererror-swift.struct.md)
  The command buffer error codes that indicate why the GPU doesn’t finish executing a command buffer.
- [struct MTLCounterSampleBufferError](mtlcountersamplebuffererror-swift.struct.md)
  The error codes that indicate why a GPU driver can’t create a counter sample buffer.
- [struct MTLDynamicLibraryError](mtldynamiclibraryerror-swift.struct.md)
  Errors when compiling dynamic libraries.
- [struct MTLIOError](mtlioerror-swift.struct.md)
  The categories of errors for creating an input/output file handle.
- [struct MTLPackedFloatQuaternion](mtlpackedfloatquaternion.md)
- [struct MTLStitchedLibraryOptions](mtlstitchedlibraryoptions.md)
- [struct NSDeviceCertification](nsdevicecertification.md)
- [struct NSProcessPerformanceProfile](nsprocessperformanceprofile.md)
  A value describing the device’s performance profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomponenttransform)*