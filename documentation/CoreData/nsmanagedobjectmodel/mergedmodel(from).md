# mergedModel(from:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns a model created by merging all the models found in given bundles.

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
class func mergedModel(from bundles: [Bundle]?) -> NSManagedObjectModel?
```

```objc
+ (NSManagedObjectModel *) mergedModelFromBundles:(NSArray<NSBundle *> *) bundles;
```

#### Return Value

A model created by merging all the models found in `bundles`.

## Parameters

- `bundles`: An array of instances of `NSBundle` to search. If you specify `nil`, then the main bundle is searched.

## See Also

### Creating a managed object model
- [convenience init?(contentsOf: URL)](./init%28contentsof%29.md)
  Initializes the managed object model using the model file at the specified URL.
- [init()](./init%28%29.md)
  Initializes an empty managed object model.
- [class func mergedModel(from: [Bundle]?, forStoreMetadata: [String : Any]) -> NSManagedObjectModel?](./mergedmodel%28from,forstoremetadata%29.md)
  Returns a merged model from a specified array for the version information in provided metadata.
- [init?(byMerging: [NSManagedObjectModel]?)](./init%28bymerging%29.md)
  Creates a single model from an array of existing models.
- [init?(byMerging: [NSManagedObjectModel], forStoreMetadata: [String : Any])](./init%28bymerging,forstoremetadata%29.md)
  Returns, for the version information in given metadata, a model merged from a given array of models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/mergedmodel(from:))*