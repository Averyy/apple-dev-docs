# ModelConfiguration

**Framework**: SwiftData  
**Kind**: struct

A type that describes the configuration of an app’s schema or specific group of models.

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
struct ModelConfiguration
```

## Mentions

- [Syncing model data across a person’s devices](syncing-model-data-across-a-persons-devices.md)
- [Preserving your app’s model data across launches](preserving-your-apps-model-data-across-launches.md)

## Topics

### Creating a model configuration
- [init(isStoredInMemoryOnly: Bool)](modelconfiguration/init(isstoredinmemoryonly:).md)
  Creates a basic model configuration.
- [init(for: any PersistentModel.Type..., isStoredInMemoryOnly: Bool)](modelconfiguration/init(for:isstoredinmemoryonly:).md)
  Creates a model configuration for the specified model types.
- [init(String?, schema: Schema?, isStoredInMemoryOnly: Bool, allowsSave: Bool, groupContainer: ModelConfiguration.GroupContainer, cloudKitDatabase: ModelConfiguration.CloudKitDatabase)](modelconfiguration/init(_:schema:isstoredinmemoryonly:allowssave:groupcontainer:cloudkitdatabase:).md)
  Creates a named model configuration for the specified schema.
- [init(String?, schema: Schema?, url: URL, allowsSave: Bool, cloudKitDatabase: ModelConfiguration.CloudKitDatabase)](modelconfiguration/init(_:schema:url:allowssave:cloudkitdatabase:).md)
  Creates a named model configuration that specifies the on-disk location of the schema’s persistent storage.
### Accessing configuration details
- [let url: URL](modelconfiguration/url.md)
  The on-disk location of the schema’s persistent storage.
- [let name: String](modelconfiguration/name.md)
  The model configuration’s name.
- [let allowsSave: Bool](modelconfiguration/allowssave.md)
  A Boolean value that determines whether the associated persistent storage is writable.
- [let isStoredInMemoryOnly: Bool](modelconfiguration/isstoredinmemoryonly.md)
  A Boolean value that determines whether the associated persistent storage is ephemeral and exists only in memory.
### Managing schema information
- [var schema: Schema?](modelconfiguration/schema.md)
  The schema that maps model classes to the associated data in the persistent storage.
- [var id: URL](modelconfiguration/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [ModelConfiguration.ID](modelconfiguration/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Sharing and syncing the model store
- [let cloudKitContainerIdentifier: String?](modelconfiguration/cloudkitcontaineridentifier.md)
  The identifier of the configuration’s CloudKit database container.
- [let cloudKitDatabase: ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.property.md)
  The option to use when detecting the container of the preferred CloudKit database.
- [ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct.md)
  A type that describes the options for detecting a CloudKit database.
- [let groupAppContainerIdentifier: String?](modelconfiguration/groupappcontaineridentifier.md)
  The identifier of the configuration’s app group container.
- [let groupContainer: ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.property.md)
  The option to use when detecting the preferred app group container.
- [ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.struct.md)
  A type that describes the options for detecting an app group container.
### Hashing
- [func hash(into: inout Hasher)](modelconfiguration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](modelconfiguration/hashvalue.md)
  The hash value.
### Comparing model configurations
- [static func == (ModelConfiguration, ModelConfiguration) -> Bool](modelconfiguration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](modelconfiguration/customdebugstringconvertible-implementations.md)
- [DataStoreConfiguration Implementations](modelconfiguration/datastoreconfiguration-implementations.md)
- [Equatable Implementations](modelconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [DataStoreConfiguration](datastoreconfiguration.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: [ModelConfiguration]) throws](modelcontainer/init(for:migrationplan:configurations:)-1czix.md)
  Creates a model container using the specified schema, migration plan, and configurations.
- [convenience init(for: any PersistentModel.Type..., migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-8s4ts.md)
  Creates a model container using the specified model types, migration plan, and zero or more configurations.
- [convenience init(for: Schema, migrationPlan: (any SchemaMigrationPlan.Type)?, configurations: ModelConfiguration...) throws](modelcontainer/init(for:migrationplan:configurations:)-qof9.md)
  Creates a model container using the specified schema, migration plan, and zero or more configurations.
- [class Schema](schema.md)
  An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [protocol SchemaMigrationPlan](schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration)*