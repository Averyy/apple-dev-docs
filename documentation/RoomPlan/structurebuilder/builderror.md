# StructureBuilder.BuildError

**Framework**: RoomPlan  
**Kind**: enum

Errors that can occur capturedStructure merging processing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 16.0+

## Declaration

```swift
enum BuildError
```

#### Overview

The structure builder ([`StructureBuilder`](structurebuilder.md)) function [`capturedStructure(from:)`](structurebuilder/capturedstructure(from:).md) can throw an error of this type.

## Topics

### Operators
- [static func == (StructureBuilder.BuildError, StructureBuilder.BuildError) -> Bool](structurebuilder/builderror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
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
  An error that indicates one or more rooms are not in the same world space. [only for StructureBuilder]
### Instance Properties
- [var errorDescription: String?](structurebuilder/builderror/errordescription.md)
  A human-readable explanation of the error.
- [var hashValue: Int](structurebuilder/builderror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](structurebuilder/builderror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](structurebuilder/builderror/equatable-implementations.md)
- [Error Implementations](structurebuilder/builderror/error-implementations.md)
- [LocalizedError Implementations](structurebuilder/builderror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/structurebuilder/builderror)*