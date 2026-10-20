# init(entityName:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Returns a fetch request configured with a given entity name.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(entityName: String)
```

```objc
+ (instancetype) fetchRequestWithEntityName:(NSString *) entityName;
```

#### Return Value

A fetch request configured to fetch the entity named `entityName`.

#### Discussion

This method provides a convenient way to configure the entity for a fetch request without having to retrieve an [`NSEntityDescription`](../nsentitydescription.md) object. When the fetch is executed, the request uses the managed object context to find the entity with the given name. The model associated with the context’s persistent store coordinator must contain an entity named `entityName`.

## Parameters

- `entityName`: The name of the entity to fetch.

## See Also

### Related Documentation
- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
### Managing the Fetch Request’s Entity
- [init()](./init%28%29.md)
  Creates a new fetch request.
- [var entityName: String?](./entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](./entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](./includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.
- [struct NSFetchRequestResultType](../nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/init(entityname:)-5anoo)*