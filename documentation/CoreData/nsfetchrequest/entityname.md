# entityName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The name of the entity the request is configured to fetch.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var entityName: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * entityName;
```

## Discussion

The entity name property is populated whenever the NSFetchRequest is created with `NSFetchRequest/init(entityName:)` or [`init(entityName:)`](./init%28entityname%29-5anoo.md).

## See Also

### Managing the Fetch Request’s Entity
- [convenience init(entityName: String)](./init%28entityname%29-5anoo.md)
  Returns a fetch request configured with a given entity name.
- [init()](./init%28%29.md)
  Creates a new fetch request.
- [var entity: NSEntityDescription?](./entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](./includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.
- [struct NSFetchRequestResultType](../nsfetchrequestresulttype.md)
  Constants that specify the possible result types a fetch request can return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/entityname)*