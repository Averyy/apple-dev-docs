# init(from:forSourceModel:destinationModel:)

**Framework**: Core Data  
**Kind**: init

Returns the mapping model that will translate data from the source to the destination model.

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
init?(from bundles: [Bundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)
```

#### Return Value

Returns the mapping model to translate data from `sourceModel` to `destinationModel`. If a suitable mapping model cannot be found, returns `nil`.

#### Discussion

This method is a companion to the [`mergedModel(from:)`](nsmanagedobjectmodel/mergedmodel(from:).md) and [`mergedModel(from:forStoreMetadata:)`](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md) methods. In this case, the framework uses the version information from the models to locate the appropriate mapping model in the available bundles.

## Parameters

- `bundles`: An array of bundles in which to search for mapping models.
- `sourceModel`: The managed object model for the source store.
- `destinationModel`: The managed object model for the destination store.

## See Also

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
- [class func inferredMappingModel(forSourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel](nsmappingmodel/inferredmappingmodel(forsourcemodel:destinationmodel:).md)
  Returns a newly created mapping model that will migrate data from the source to the destination model.
- [init?(contentsOf: URL?)](nsmappingmodel/init(contentsof:).md)
  Returns a mapping model initialized from a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel/init(from:forsourcemodel:destinationmodel:))*