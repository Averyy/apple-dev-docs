# Staged migrations

**Framework**: Core Data

Migrate complex data models containing changes that are incompatible with lightweight migrations.

#### Overview

Core Data uses lightweight migrations to keep the data in your app’s persistent store consistent with the app’s managed object model. A lightweight migration automatically determines the differences between two model versions and generates a mapping model that Core Data then uses to make the necessary changes to the persistent store. Lightweight migrations support a number of common operations, such as adding an entity, removing a relationship, changing a nonoptional attribute to an optional attribute, renaming an entity, and so on.

As your object model evolves, you may find that the aggregate changes between two model versions exceed the capabilities of lightweight migrations. For example, if you change an optional attribute to be nonoptional, there’s no way for a lightweight migration to infer the default value it needs to assign to any instances of that attribute with a `nil` value.

 solve this problem by reducing an incompatible migration into a series of compatible stages. A migration manager runs these stages in a specific order, providing opportunities for you to prepare the persistent store before each stage runs, and perform any cleanup afterward. This enables you to handle scenarios like changing an optional attribute to be nonoptional because you have an opportunity to set any `nil` values to a concrete value before the stage runs.

> ❗ **Important**:  Successful Core Data migrations depend on properly versioned object models, and staged lightweight migrations require a distinct migration stage for each model version.

## Topics

### Migration staging
- [let NSPersistentStoreStagedMigrationManagerOptionKey: String](nspersistentstorestagedmigrationmanageroptionkey.md)
  The key for specifying your staged migration manager.
- [class NSStagedMigrationManager](nsstagedmigrationmanager.md)
  An object that handles the migration event loop and provides access to the migrating persistent store.
### Migration stages
- [class NSLightweightMigrationStage](nslightweightmigrationstage.md)
  An object that describes a series of models suitable for lightweight migration.
- [class NSCustomMigrationStage](nscustommigrationstage.md)
  An object that enables you to participate in the migration between two versions of the same model.
- [class NSMigrationStage](nsmigrationstage.md)
  An abstract base class for describing an individual stage of a migration.

## See Also

- [Migrating your data model automatically](migrating-your-data-model-automatically.md)
  Enable lightweight migrations to keep your data model and the underlying data in a consistent state.
- [Manual migrations](manual-migrations.md)
  Migrate elaborate data models with changes that go beyond the capabilities of both lightweight and staged migrations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/staged-migrations)*