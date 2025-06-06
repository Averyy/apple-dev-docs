# init(byMerging:forStoreMetadata:)

**Framework**: Core Data  
**Kind**: init

Returns, for the version information in given metadata, a model merged from a given array of models.

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
init?(byMerging models: [NSManagedObjectModel], forStoreMetadata metadata: [String : Any])
```

#### Return Value

A  merged model from `models` for the version information in `metadata`. If a model cannot be created to match the version information in `metadata`, returns `nil`.

#### Discussion

This is the companion method to [`mergedModel(from:forStoreMetadata:)`](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md).

## Parameters

- `models`: An array of instances of  .
- `metadata`: A dictionary containing version information from the metadata for a persistent store.

## See Also

- [convenience init?(contentsOf: URL)](nsmanagedobjectmodel/init(contentsof:).md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](nsmanagedobjectmodel/init.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:).md)
  Returns a model created by merging all the models found in given bundles.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](nsmanagedobjectmodel/init(bymerging:).md)
  Creates a single model from an array of existing models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init(bymerging:forstoremetadata:))*