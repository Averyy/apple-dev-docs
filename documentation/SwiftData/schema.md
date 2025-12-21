# Schema

**Framework**: SwiftData  
**Kind**: class

An object that maps model classes to data in the model store, and helps with the migration of that data between releases.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
final class Schema
```

## Topics

### Creating a schema
- [init(Schema.Entity..., version: Schema.Version)](schema/init(_:version:)-8el78.md)
- [init([any PersistentModel.Type], version: Schema.Version)](schema/init(_:version:)-8jo9o.md)
- [convenience init(versionedSchema: any VersionedSchema.Type)](schema/init(versionedschema:).md)
- [protocol VersionedSchema](versionedschema.md)
  An interface for describing a specific version of a schema, including the models it contains.
- [init()](schema/init.md)
- [Schema components](schemacomponents.md)
  Specify the constituent parts of your schema, including entities, attributes, and relationships.
### Accessing entities
- [let entities: [Schema.Entity]](schema/entities.md)
- [let entitiesByName: [String : Schema.Entity]](schema/entitiesbyname.md)
- [Schema.Entity](schema/entity.md)
  An object that provides a blueprint for the associated model class.
### Accessing version details
- [static let schemaEncodingVersion: Schema.Version](schema/schemaencodingversion.md)
- [let encodingVersion: Schema.Version](schema/encodingversion.md)
### Saving and loading
- [func save(to: URL) throws](schema/save(to:).md)
- [static func load(from: URL) throws -> Schema](schema/load(from:).md)
### Classes
- [Schema.Index](schema/index.md)
- [Schema.Unique](schema/unique.md)
### Structures
- [Schema.PropertyMetadata](schema/propertymetadata.md)
- [Schema.Version](schema/version-swift.struct.md)
### Initializers
- [convenience init(any PersistentModel.Type..., version: Schema.Version)](schema/init(_:version:)-1aea5.md)
### Instance Properties
- [let version: Schema.Version](schema/version-swift.property.md)
### Instance Methods
- [func entity<T>(for: T.Type) -> Schema.Entity?](schema/entity(for:).md)
### Type Methods
- [static func entityName<T>(for: T.Type) -> String](schema/entityname(for:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](modelcontainer/init(for:migrationplan:configurations:)-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [convenience init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-qof9.md)
  Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [protocol PersistentModel](persistentmodel.md)
  An interface that enables SwiftData to manage a Swift class as a stored model.
- [struct ModelConfiguration](modelconfiguration.md)
  A type that describes the configuration of an app’s schema or specific group of models.
- [protocol SchemaMigrationPlan](schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema)*