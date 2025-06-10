# NSMigrationStage

**Framework**: Core Data  
**Kind**: class

An abstract base class for describing an individual stage of a migration.

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
class NSMigrationStage
```

#### Overview

> ❗ **Important**:  Don’t create instances of [`NSMigrationStage`](nsmigrationstage.md). Instead, use a concrete subclass, such as [`NSLightweightMigrationStage`](nslightweightmigrationstage.md) or [`NSCustomMigrationStage`](nscustommigrationstage.md).

## Topics

### Describing the purpose
- [var label: String!](nsmigrationstage/label.md)
  The textual description of the migration stage’s purpose.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSCustomMigrationStage](nscustommigrationstage.md)
- [NSLightweightMigrationStage](nslightweightmigrationstage.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSLightweightMigrationStage](nslightweightmigrationstage.md)
  An object that describes a series of models suitable for lightweight migration.
- [class NSCustomMigrationStage](nscustommigrationstage.md)
  An object that enables you to participate in the migration between two versions of the same model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationstage)*