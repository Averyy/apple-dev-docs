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
### Encoding and decoding
- [func encode(to: any Encoder) throws](schema/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](schema/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Hashing
- [func hash(into: inout Hasher)](schema/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing schemas
- [static func == (Schema, Schema) -> Bool](schema/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Classes
- [Schema.Index](schema/index.md)
- [Schema.Unique](schema/unique.md)
### Structures
- [Schema.PropertyMetadata](schema/propertymetadata.md)
- [Schema.Version](schema/version-swift.struct.md)
### Instance Properties
- [var hashValue: Int](schema/hashvalue.md)
  The hash value.
- [let version: Schema.Version](schema/version-swift.property.md)
### Instance Methods
- [func entity<T>(for: T.Type) -> Schema.Entity?](schema/entity(for:).md)
### Type Methods
- [static func entityName<T>(for: T.Type) -> String](schema/entityname(for:).md)
### Default Implementations
- [CustomDebugStringConvertible Implementations](schema/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](schema/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](modelcontainer/init(for:migrationplan:configurations:)-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [convenience init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-qof9.md)
  Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [struct ModelConfiguration](modelconfiguration.md)
  A type that describes the configuration of an app’s schema or specific group of models.
- [protocol SchemaMigrationPlan](schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema)*