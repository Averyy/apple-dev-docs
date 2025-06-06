# mergedModel(from:forStoreMetadata:)

**Framework**: Core Data  
**Kind**: method

Returns a merged model from a specified array for the version information in provided metadata.

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
class func mergedModel(from bundles: [Bundle]?, forStoreMetadata metadata: [String : Any]) -> NSManagedObjectModel?
```

#### Return Value

The managed object model used to create the store for the metadata. If a model cannot be created to match the version information specified by `metadata`, returns `nil`.

#### Discussion

This method is a companion to [`mergedModel(from:)`](nsmanagedobjectmodel/mergedmodel(from:).md).

## Parameters

- `bundles`: An array of bundles.
- `metadata`: A dictionary containing version information from the metadata for a persistent store.

## See Also

- [convenience init?(contentsOf: URL)](nsmanagedobjectmodel/init(contentsof:).md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](nsmanagedobjectmodel/init.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:).md)
  Returns a model created by merging all the models found in given bundles.
- [init?(byMerging: [NSManagedObjectModel]?)](nsmanagedobjectmodel/init(bymerging:).md)
  Creates a single model from an array of existing models.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](nsmanagedobjectmodel/init(bymerging:forstoremetadata:).md)
  Returns, for the version information in given metadata, a model merged from a given array of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:))*