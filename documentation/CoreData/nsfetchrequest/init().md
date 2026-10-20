# init()

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a new fetch request.

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

### Managing the Fetch Request’s Entity
- [convenience init(entityName: String)](./init%28entityname%29-5anoo.md)
  Returns a fetch request configured with a given entity name.
- [var entityName: String?](./entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](./entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](./includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.
- [struct NSFetchRequestResultType](../nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/init())*