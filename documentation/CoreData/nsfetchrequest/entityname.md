# entityName

**Framework**: Core Data  
**Kind**: property

The name of the entity the request is configured to fetch.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var entityName: String? { get }
```

#### Discussion

The entity name property is populated whenever the NSFetchRequest is created with [`init(entityName:)`](nsfetchrequest/init(entityname:).md) or [`fetchRequestWithEntityName:`](nsfetchrequest/fetchrequestwithentityname:.md).

## See Also

- [init()](nsfetchrequest/init.md)
  Creates a new fetch request.
- [convenience init(entityName: String)](nsfetchrequest/init(entityname:).md)
  Initializes a fetch request configured with a given entity name.
- [var entity: NSEntityDescription?](nsfetchrequest/entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](nsfetchrequest/includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/entityname)*