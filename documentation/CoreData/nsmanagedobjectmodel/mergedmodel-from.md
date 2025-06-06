# mergedModel(from:)

**Framework**: Core Data  
**Kind**: method

Returns a model created by merging all the models found in given bundles.

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
class func mergedModel(from bundles: [Bundle]?) -> NSManagedObjectModel?
```

#### Return Value

A model created by merging all the models found in `bundles`.

## Parameters

- `bundles`: An array of instances of   to search. If you specify  , then the main bundle is searched.

## See Also

- [convenience init?(contentsOf: URL)](nsmanagedobjectmodel/init(contentsof:).md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](nsmanagedobjectmodel/init.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](nsmanagedobjectmodel/init(bymerging:).md)
  Creates a single model from an array of existing models.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](nsmanagedobjectmodel/init(bymerging:forstoremetadata:).md)
  Returns, for the version information in given metadata, a model merged from a given array of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:))*