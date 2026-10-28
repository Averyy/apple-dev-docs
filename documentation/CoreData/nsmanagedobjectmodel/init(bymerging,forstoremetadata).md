# init(byMerging:forStoreMetadata:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Returns, for the version information in given metadata, a model merged from a given array of models.

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
init?(byMerging models: [NSManagedObjectModel], forStoreMetadata metadata: [String : Any])
```

```objc
+ (NSManagedObjectModel *) modelByMergingModels:(NSArray<NSManagedObjectModel *> *) models forStoreMetadata:(NSDictionary<NSString *,id> *) metadata;
```

## Return Value

A  merged model from `models` for the version information in `metadata`. If a model cannot be created to match the version information in `metadata`, returns `nil`.

## Discussion

This is the companion method to [`mergedModel(from:forStoreMetadata:)`](./mergedmodel%28from,forstoremetadata%29.md).

## Parameters

- `models`: An array of instances of `NSManagedObjectModel`.
- `metadata`: A dictionary containing version information from the metadata for a persistent store.

## See Also

### Creating a managed object model
- [convenience init?(contentsOf: URL)](./init%28contentsof%29.md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](./init%28%29.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?) -> NSManagedObjectModel?](./mergedmodel%28from%29.md)
  Returns a model created by merging all the models found in given bundles.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](./mergedmodel%28from,forstoremetadata%29.md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](./init%28bymerging%29.md)
  Creates a single model from an array of existing models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/init(bymerging:forstoremetadata:))*