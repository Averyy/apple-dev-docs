# NSInferMappingModelAutomaticallyOption

**Framework**: Core Data  
**Kind**: var

Key to attempt to create the mapping model automatically.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSInferMappingModelAutomaticallyOption: String
```

## Mentions

- [Migrating your data model automatically](migrating-your-data-model-automatically.md)

#### Discussion

The corresponding value is an `NSNumber` object. If the [`boolValue`](https://developer.apple.com/documentation/Foundation/NSNumber/boolValue) of the number is [`true`](https://developer.apple.com/documentation/Swift/true) and the value of the `NSMigratePersistentStoresAutomaticallyOption` is [`true`](https://developer.apple.com/documentation/Swift/true), the coordinator will attempt to infer a mapping model if none can be found.

## See Also

- [let NSIgnorePersistentStoreVersioningOption: String](nsignorepersistentstoreversioningoption.md)
  Key to ignore the built-in versioning provided by Core Data.
- [let NSMigratePersistentStoresAutomaticallyOption: String](nsmigratepersistentstoresautomaticallyoption.md)
  Key to automatically attempt to migrate versioned stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsinfermappingmodelautomaticallyoption)*