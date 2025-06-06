# includesSubentities

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the fetch request includes subentities in the results.

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
var includesSubentities: Bool { get set }
```

#### Discussion

The value is [`true`](https://developer.apple.com/documentation/swift/true) if the request will include all subentities of the entity for the request; otherwise it is [`false`](https://developer.apple.com/documentation/swift/false). The default is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [init()](nsfetchrequest/init.md)
  Creates a new fetch request.
- [convenience init(entityName: String)](nsfetchrequest/init(entityname:).md)
  Initializes a fetch request configured with a given entity name.
- [var entityName: String?](nsfetchrequest/entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](nsfetchrequest/entity.md)
  The entity specified for the fetch request.
- [struct NSFetchRequestResultType](nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/includessubentities)*