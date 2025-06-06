# entity

**Framework**: Core Data  
**Kind**: property

The entity specified for the fetch request.

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
var entity: NSEntityDescription? { get set }
```

#### Discussion

When an [`NSFetchRequest`](nsfetchrequest.md) instance is created with `init()`, it is expected that the [`entity`](nspropertydescription/entity.md) property will be set.  If this property is not set, the fetch request fails upon execution.

## See Also

- [init()](nsfetchrequest/init.md)
  Creates a new fetch request.
- [convenience init(entityName: String)](nsfetchrequest/init(entityname:).md)
  Initializes a fetch request configured with a given entity name.
- [var entityName: String?](nsfetchrequest/entityname.md)
  The name of the entity the request is configured to fetch.
- [var includesSubentities: Bool](nsfetchrequest/includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/entity)*