# init()

**Framework**: Core Data  
**Kind**: init

Initializes an empty managed object model.

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
init()
```

## See Also

- [convenience init?(contentsOf: URL)](nsmanagedobjectmodel/init(contentsof:).md)
  Initializes the managed object model using the model file at the specified URL.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:).md)
  Returns a model created by merging all the models found in given bundles.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](nsmanagedobjectmodel/mergedmodel(from:forstoremetadata:).md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](nsmanagedobjectmodel/init(bymerging:).md)
  Creates a single model from an array of existing models.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](nsmanagedobjectmodel/init(bymerging:forstoremetadata:).md)
  Returns, for the version information in given metadata, a model merged from a given array of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init())*