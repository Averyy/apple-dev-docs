# init(byMerging:)

**Framework**: Core Data  
**Kind**: init

Creates a single model from an array of existing models.

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
init?(byMerging models: [NSManagedObjectModel]?)
```

#### Return Value

A single model made by combining the models in `models`.

#### Discussion

You use this method to combine multiple models (typically from different frameworks) into one.

## Parameters

- `models`: An array of instances of  .

## See Also

- [convenience init?(contentsOf: URL)](nsmanagedobjectmodel/init(contentsof:).md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](nsmanagedobjectmodel/init.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:).md)
  Returns a model created by merging all the models found in given bundles.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](nsmanagedobjectmodel/init(bymerging:forstoremetadata:).md)
  Returns, for the version information in given metadata, a model merged from a given array of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init(bymerging:))*