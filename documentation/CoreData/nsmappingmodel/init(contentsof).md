# init(contentsOf:)

**Framework**: Core Data  
**Kind**: init

Returns a mapping model initialized from a given URL.

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
init?(contentsOf url: URL?)
```

#### Return Value

A mapping model initialized from `url`.

## Parameters

- `url`: The location of an archived mapping model.

## See Also

- [init?(from: [Bundle]?, forSourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)](nsmappingmodel/init(from:forsourcemodel:destinationmodel:).md)
  Returns the mapping model that will translate data from the source to the destination model.
- [class func inferredMappingModel(forSourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel](nsmappingmodel/inferredmappingmodel(forsourcemodel:destinationmodel:).md)
  Returns a newly created mapping model that will migrate data from the source to the destination model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel/init(contentsof:))*