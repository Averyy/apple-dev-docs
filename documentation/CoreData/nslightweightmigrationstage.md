# NSLightweightMigrationStage

**Framework**: Core Data  
**Kind**: class

An object that describes a series of models suitable for lightweight migration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class NSLightweightMigrationStage
```

#### Overview

Use [`NSLightweightMigrationStage`](nslightweightmigrationstage.md) when you have a series of models to migrate and those models are compatible with lightweight migrations. Instances of this class supplement your custom migration stages and help maintain a consistent stage order for the entire migration.

## Topics

### Creating a migration stage
- [convenience init([String])](nslightweightmigrationstage/init(_:).md)
  Creates a lightweight migration stage with the specified version checksums.
### Accessing the checksums
- [var versionChecksums: [String]](nslightweightmigrationstage/versionchecksums.md)
  The array of version checksums.

## Relationships

### Inherits From
- [NSMigrationStage](nsmigrationstage.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCustomMigrationStage](nscustommigrationstage.md)
  An object that enables you to participate in the migration between two versions of the same model.
- [class NSMigrationStage](nsmigrationstage.md)
  An abstract base class for describing an individual stage of a migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nslightweightmigrationstage)*