# StructureBuilder.BuildError

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur during the multiple-scan merging process.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
enum BuildError
```

#### Overview

The structure builder ([`StructureBuilder`](../structurebuilder.md)) function [`capturedStructure(from:)`](./capturedstructure%28from%29.md) throws an error of this type if the multiple-scan merging process fails.

## Topics

### Enumeration Cases
- [StructureBuilder.BuildError.deviceNotSupported](./builderror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [StructureBuilder.BuildError.exceedSceneSizeLimit](./builderror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [StructureBuilder.BuildError.insufficientInput](./builderror/insufficientinput.md)
  An error that indicates the framework expects more captured room data.
- [StructureBuilder.BuildError.internalError](./builderror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
- [StructureBuilder.BuildError.invalidInput](./builderror/invalidinput.md)
  An error that indicates the framework encounters invalid captured room data.
- [StructureBuilder.BuildError.invalidRoomLocation](./builderror/invalidroomlocation.md)
  An error that indicates one or more rooms reside in a different vicinity.
### Instance Properties
- [var errorDescription: String?](./builderror/errordescription.md)
  A human-readable explanation of the error.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/structurebuilder/builderror)*