# NSInferMappingModelAutomaticallyOption

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

Key to attempt to create the mapping model automatically.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSInferMappingModelAutomaticallyOption: String
```

```c
extern NSString * const NSInferMappingModelAutomaticallyOption;
```

## Mentions

- [Migrating your data model automatically](./migrating-your-data-model-automatically.md)

## Discussion

The corresponding value is an `NSNumber` object. If the [`boolValue`](../Foundation/nsnumber/boolvalue.md) of the number is [`true`](../Swift/true.md) and the value of the `NSMigratePersistentStoresAutomaticallyOption` is [`true`](../Swift/true.md), the coordinator will attempt to infer a mapping model if none can be found.

## See Also

### Constants
- [let NSIgnorePersistentStoreVersioningOption: String](./nsignorepersistentstoreversioningoption.md)
  Key to ignore the built-in versioning provided by Core Data.
- [let NSMigratePersistentStoresAutomaticallyOption: String](./nsmigratepersistentstoresautomaticallyoption.md)
  Key to automatically attempt to migrate versioned stores.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsinfermappingmodelautomaticallyoption)*