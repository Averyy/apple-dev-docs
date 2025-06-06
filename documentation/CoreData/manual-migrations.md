# Manual migrations

**Framework**: Core Data

Migrate elaborate data models with changes that go beyond the capabilities of both lightweight and staged migrations.

## Topics

### Entity Mapping
- [class NSMigrationManager](nsmigrationmanager.md)
  A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [class NSMappingModel](nsmappingmodel.md)
  A model instance that specifies how to map a model from a source to a destination managed object model.
- [class NSEntityMapping](nsentitymapping.md)
  A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [class NSEntityMigrationPolicy](nsentitymigrationpolicy.md)
  A policy instance that customizes the migration process for an entity mapping.
- [enum NSEntityMappingType](nsentitymappingtype.md)
  The types for mapping an entity between a source model and a destination model.
- [class NSPropertyMapping](nspropertymapping.md)
  A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.

## See Also

- [Migrating your data model automatically](migrating-your-data-model-automatically.md)
  Enable lightweight migrations to keep your data model and the underlying data in a consistent state.
- [Staged migrations](staged-migrations.md)
  Migrate complex data models containing changes that are incompatible with lightweight migrations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/manual-migrations)*