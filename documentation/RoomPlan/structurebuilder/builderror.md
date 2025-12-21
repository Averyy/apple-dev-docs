# StructureBuilder.BuildError

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur during the multiple-scan merging process.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS ?+

## Declaration

```swift
enum BuildError
```

#### Overview

The structure builder ([`StructureBuilder`](structurebuilder.md)) function [`capturedStructure(from:)`](structurebuilder/capturedstructure(from:).md) throws an error of this type if the multiple-scan merging process fails.

## Topics

### Enumeration Cases
- [StructureBuilder.BuildError.deviceNotSupported](structurebuilder/builderror/devicenotsupported.md)
  An error that indicates that the framework doesn’t support the user’s device.
- [StructureBuilder.BuildError.exceedSceneSizeLimit](structurebuilder/builderror/exceedscenesizelimit.md)
  An error that indicates when the scene size grows past the framework’s limitations.
- [StructureBuilder.BuildError.insufficientInput](structurebuilder/builderror/insufficientinput.md)
  An error that indicates the framework expects more captured room data.
- [StructureBuilder.BuildError.internalError](structurebuilder/builderror/internalerror.md)
  An error that indicates when the framework encounters an unexpected error case.
- [StructureBuilder.BuildError.invalidInput](structurebuilder/builderror/invalidinput.md)
  An error that indicates the framework encounters invalid captured room data.
- [StructureBuilder.BuildError.invalidRoomLocation](structurebuilder/builderror/invalidroomlocation.md)
  An error that indicates one or more rooms reside in a different vicinity.
### Instance Properties
- [var errorDescription: String?](structurebuilder/builderror/errordescription.md)
  A human-readable explanation of the error.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/structurebuilder/builderror)*