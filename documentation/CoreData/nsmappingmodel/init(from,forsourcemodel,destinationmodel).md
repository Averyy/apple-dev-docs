# init(from:forSourceModel:destinationModel:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Returns the mapping model that will translate data from the source to the destination model.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(from bundles: [Bundle]?, forSourceModel sourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)
```

```objc
+ (NSMappingModel *) mappingModelFromBundles:(NSArray<NSBundle *> *) bundles forSourceModel:(NSManagedObjectModel *) sourceModel destinationModel:(NSManagedObjectModel *) destinationModel;
```

## Return Value

Returns the mapping model to translate data from `sourceModel` to `destinationModel`. If a suitable mapping model cannot be found, returns `nil`.

## Discussion

This method is a companion to the [`mergedModel(from:)`](../nsmanagedobjectmodel/mergedmodel%28from%29.md) and [`mergedModel(from:forStoreMetadata:)`](../nsmanagedobjectmodel/mergedmodel%28from,forstoremetadata%29.md) methods. In this case, the framework uses the version information from the models to locate the appropriate mapping model in the available bundles.

## Parameters

- `bundles`: An array of bundles in which to search for mapping models.
- `sourceModel`: The managed object model for the source store.
- `destinationModel`: The managed object model for the destination store.

## See Also

### Related Documentation
- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
### Creating a Mapping
- [class func inferredMappingModel(forSourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel](./inferredmappingmodel%28forsourcemodel,destinationmodel%29.md)
  Returns a newly created mapping model that will migrate data from the source to the destination model.
- [init?(contentsOf: URL?)](./init%28contentsof%29.md)
  Returns a mapping model initialized from a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel/init(from:forsourcemodel:destinationmodel:))*