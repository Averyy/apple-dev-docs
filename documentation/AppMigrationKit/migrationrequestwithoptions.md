# MigrationRequestWithOptions

**Framework**: AppMigrationKit  
**Kind**: struct

An object that exposes properties of the migration request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
struct MigrationRequestWithOptions<OptionsType> where OptionsType : CaseIterable, OptionsType : Hashable, OptionsType : RawRepresentable, OptionsType : Sendable, OptionsType.RawValue == String
```

## Topics

### Creating a migration request instance
- [init(destinationPlatform: MigrationPlatform, options: [OptionsType : Data])](migrationrequestwithoptions/init(destinationplatform:options:).md)
  Creates a request instance.
### Inspecting migration request properties
- [let destinationPlatform: MigrationPlatform](migrationrequestwithoptions/destinationplatform.md)
  The destination platform of the migration request.
- [struct MigrationPlatform](migrationplatform.md)
  A type that identifies the platform used by the other device in a migration.
- [let options: [OptionsType : Data]](migrationrequestwithoptions/options.md)
  Export options requested by the destination device.
### Declaring default options
- [enum MigrationDefaultSupportedOptions](migrationdefaultsupportedoptions.md)
  Options supported by default for migration requests.
- [typealias MigrationRequest](migrationrequest.md)
  A migration request that uses the default supported options.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func exportResources(to: sending ResourcesArchiver, request: MigrationRequestWithOptions<Self.OptionsType>) async throws](resourcesexportingwithoptions/exportresources(to:request:).md)
  Exports resources from the app, in response to a request from the migration system.
- [class ResourcesArchiver](resourcesarchiver.md)
  An object your app uses to archive resources during an export operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/migrationrequestwithoptions)*