# inferredMappingModel(forSourceModel:destinationModel:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Returns a newly created mapping model that will migrate data from the source to the destination model.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func inferredMappingModel(forSourceModel sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel
```

```objc
+ (NSMappingModel *) inferredMappingModelForSourceModel:(NSManagedObjectModel *) sourceModel destinationModel:(NSManagedObjectModel *) destinationModel error:(NSError **) error;
```

## Mentions

- [Migrating your data model automatically](../migrating-your-data-model-automatically.md)

#### Return Value

A newly-created mapping model to migrate data from the source to the destination model. If the mapping model can not be created, returns `nil`.

#### Discussion

A model will be created only if all changes are simple enough to be able to reasonably infer a mapping (for example, removing or renaming an attribute, adding an optional attribute or relationship, or adding renaming or deleting an entity). Element IDs are used to track renamed properties and entities.

## Parameters

- `sourceModel`: The source managed object model.
- `destinationModel`: The destination managed object model.

## See Also

### Creating a Mapping
- [init?(from: [Bundle]?, forSourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)](./init%28from,forsourcemodel,destinationmodel%29.md)
  Returns the mapping model that will translate data from the source to the destination model.
- [init?(contentsOf: URL?)](./init%28contentsof%29.md)
  Returns a mapping model initialized from a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel/inferredmappingmodel(forsourcemodel:destinationmodel:))*