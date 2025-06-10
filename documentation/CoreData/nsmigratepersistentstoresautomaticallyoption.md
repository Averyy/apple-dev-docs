# NSMigratePersistentStoresAutomaticallyOption

**Framework**: Core Data  
**Kind**: var

Key to automatically attempt to migrate versioned stores.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSMigratePersistentStoresAutomaticallyOption: String
```

## Mentions

- [Migrating your data model automatically](migrating-your-data-model-automatically.md)

#### Discussion

The corresponding value is an `NSNumber` object. If the [`boolValue`](https://developer.apple.com/documentation/Foundation/NSNumber/boolValue) of the number is [`true`](https://developer.apple.com/documentation/swift/true) and if the version hash information for the added store is determined to be incompatible with the model for the coordinator, Core Data will attempt to locate the source and mapping models in the application bundles, and perform a migration.

## See Also

- [let NSIgnorePersistentStoreVersioningOption: String](nsignorepersistentstoreversioningoption.md)
  Key to ignore the built-in versioning provided by Core Data.
- [let NSInferMappingModelAutomaticallyOption: String](nsinfermappingmodelautomaticallyoption.md)
  Key to attempt to create the mapping model automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigratepersistentstoresautomaticallyoption)*