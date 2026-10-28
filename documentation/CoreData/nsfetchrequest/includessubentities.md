# includesSubentities

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the fetch request includes subentities in the results.

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
var includesSubentities: Bool { get set }
```

```objc
@property (nonatomic) BOOL includesSubentities;
```

## Discussion

The value is [`true`](../../Swift/true.md) if the request will include all subentities of the entity for the request; otherwise it is [`false`](../../Swift/false.md). The default is [`true`](../../Swift/true.md).

## See Also

### Managing the Fetch Request’s Entity
- [convenience init(entityName: String)](./init%28entityname%29-5anoo.md)
  Returns a fetch request configured with a given entity name.
- [init()](./init%28%29.md)
  Creates a new fetch request.
- [var entityName: String?](./entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](./entity.md)
  The entity specified for the fetch request.
- [struct NSFetchRequestResultType](../nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/includessubentities)*