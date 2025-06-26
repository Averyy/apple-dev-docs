# ModelContainer

**Framework**: SwiftData  
**Kind**: class

An object that manages an app’s schema and model storage configuration.

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
class ModelContainer
```

## Mentions

- [Reverting data changes using the undo manager](reverting-data-changes-using-the-undo-manager.md)
- [Syncing model data across a person’s devices](syncing-model-data-across-a-persons-devices.md)

#### Overview

A model container mediates between its associated model contexts and your app’s underlying persistent storage. The container manages all aspects of that storage and ensures it remains in a consistent and usable state. Whenever you run a fetch or call a context’s [`save()`](modelcontext/save().md) method, the container performs the actual read or write of the underlying data using information from the schema you provide. This helps safeguard an app’s resources and ensures those operations happen only in an efficient and coordinated manner. Additionally, if your app’s entitlements include CloudKit, the container automatically handles syncing the persisted storage across devices. For more information about syncing model data, see [`Syncing model data across a person’s devices`](syncing-model-data-across-a-persons-devices.md).

As your app’s schema evolves, the container performs automatic migrations of the persisted model data so it remains consistent with the app’s model classes. If the aggregate changes between two versions of your schema exceed the capabilities of automatic migrations, provide the container with a [`SchemaMigrationPlan`](schemamigrationplan.md) to participate in those migrations and help ensure they complete successfully.

By default, a model container makes a number of assumptions about how it configures an app’s persistent storage. If you need to customize this behavior, provide the container with one or more instances of [`ModelConfiguration`](modelconfiguration.md). For example, you may want use a particular app group container or specify that the storage is ephemeral and should exist only in memory.

An app that uses SwiftData requires at least one model container. You create a container using one of the class’s initializers or the corresponding SwiftUI view modifier. Using the view modifier ensures all windows in the modified window group, or all child views of the modified view, access the same model container. Additionally, the view modifier makes an associated model context available in the SwiftUI environment, which the `Query()` macro depends on.

```swift
@main
struct RecipesApp: App {
    var body: some Scene {
        WindowGroup {
            RecipesList()
        }
        .modelContainer(for: Recipe.self)
    }
}

struct RecipesList: View {
    @Query private var recipes: [Recipe]
    
    var body: some View {
        List(recipes) { RecipeRowView($0) }
    }
} 

```

## Topics

### Creating a model container
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
- [class Schema](schema.md)
  An object that maps model classes to data in the model store, and helps with the migration of that data between releases.
- [protocol SchemaMigrationPlan](schemamigrationplan.md)
  An interface for describing the evolution of a schema and how to migrate between specific versions.
### Managing schema and configuration details
- [let schema: Schema](modelcontainer/schema.md)
  The schema that maps your app’s model classes to the associated data in the app’s persistent storage.
- [var configurations: Set<ModelConfiguration>](modelcontainer/configurations.md)
  The configurations that describe how to manage the persisted data for specific groups of models.
- [let migrationPlan: (any SchemaMigrationPlan.Type)?](modelcontainer/migrationplan.md)
  The plan that describes the evolution of your app’s schema and how to migrate between specific versions.
### Accessing the context
- [var mainContext: ModelContext](modelcontainer/maincontext.md)
  A model context that’s bound to app’s main actor.
### Deleting the container
- [func deleteAllData()](modelcontainer/deletealldata.md)
  Removes all persisted model data from the app’s persistent storage.
### Comparing model containers
- [static func == (ModelContainer, ModelContainer) -> Bool](modelcontainer/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [convenience init(for: any PersistentModel.Type..., configurations: any DataStoreConfiguration...) throws](modelcontainer/init(for:configurations:)-621ei.md)
- [init(for: Schema, configurations: [any DataStoreConfiguration]) throws](modelcontainer/init(for:configurations:)-93ifi.md)
### Instance Methods
- [func erase() throws](modelcontainer/erase.md)
### Default Implementations
- [Equatable Implementations](modelcontainer/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ModelContext](modelcontext.md)
  An object that enables you to fetch, insert, and delete models, and save any changes to disk.
- [Fetching and filtering time-based model changes](fetching-and-filtering-time-based-model-changes.md)
  Track all inserts, updates, and deletes that occur in a data store and process them as a series of chronological transactions.
- [struct HistoryDescriptor](historydescriptor.md)
  A type that describes the criteria, and, optionally, sort order, to use when fetching history data
- [Deleting persistent data from your app](deleting-persistent-data-from-your-app.md)
  Explore different ways to use SwiftData to delete persistent data.
- [Reverting data changes using the undo manager](reverting-data-changes-using-the-undo-manager.md)
  Automatically record data change operations that people perform in your SwiftUI app, and let them undo and redo those changes.
- [Syncing model data across a person’s devices](syncing-model-data-across-a-persons-devices.md)
  Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app’s model data using iCloud.
- [Concurrency support](concurrencysupport.md)
  Types you use to access model attributes and perform storage-related tasks in a safe and isolated way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelcontainer)*