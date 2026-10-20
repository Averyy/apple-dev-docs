# init()

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Initializes an empty managed object model.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## See Also

### Creating a managed object model
- [convenience init?(contentsOf: URL)](./init%28contentsof%29.md)
  Initializes the managed object model using the model file at the specified URL.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](./mergedmodel%28from%29.md)
  Returns a model created by merging all the models found in given bundles.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](./mergedmodel%28from,forstoremetadata%29.md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](./init%28bymerging%29.md)
  Creates a single model from an array of existing models.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](./init%28bymerging,forstoremetadata%29.md)
  Returns, for the version information in given metadata, a model merged from a given array of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init())*