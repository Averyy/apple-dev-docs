# init(managedObjectModel:)

**Framework**: Core Data  
**Kind**: init

Creates a persistent store coordinator with the specified managed object model.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(managedObjectModel model: NSManagedObjectModel)
```

#### Return Value

The receiver, initialized with `model`.

## Parameters

- `model`: A managed object model.

## See Also

- [Store options](store-options.md)
  The options keys that configure the behavior and characteristics of a persistent store.
- [Migration options](migration-options.md)
  The options keys that configure the migration behavior of a persistent store.
- [Store versions](store-versions.md)
  The metadata keys you use when comparing store versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/init(managedobjectmodel:))*