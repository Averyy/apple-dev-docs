# NSIgnorePersistentStoreVersioningOption

**Framework**: Core Data  
**Kind**: var

Key to ignore the built-in versioning provided by Core Data.

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
let NSIgnorePersistentStoreVersioningOption: String
```

#### Discussion

The corresponding value is an `NSNumber` object. If the [`boolValue`](https://developer.apple.com/documentation/Foundation/NSNumber/boolValue) of the number is [`true`](https://developer.apple.com/documentation/swift/true), Core Data will not compare the version hashes between the managed object model in the coordinator and the metadata for the loaded store. (It will, however, continue to update the version hash information in the metadata.) This key and corresponding value of [`true`](https://developer.apple.com/documentation/swift/true) is specified by default for all applications linked on or before OS X v10.4.

## See Also

- [let NSMigratePersistentStoresAutomaticallyOption: String](nsmigratepersistentstoresautomaticallyoption.md)
  Key to automatically attempt to migrate versioned stores.
- [let NSInferMappingModelAutomaticallyOption: String](nsinfermappingmodelautomaticallyoption.md)
  Key to attempt to create the mapping model automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsignorepersistentstoreversioningoption)*