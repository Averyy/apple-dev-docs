# entityName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The name of the managed entity to update data for.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var entityName: String { get }
```

```objc
@property (copy, readonly) NSString * entityName;
```

## See Also

### Configuring a Request
- [var entity: NSEntityDescription](./entity.md)
  The managed entity to update data for.
- [var includesSubentities: Bool](./includessubentities.md)
  A Boolean value that indicates whether to update subentities.
- [var predicate: NSPredicate?](./predicate.md)
  A predicate that identifies the objects to update.
- [var propertiesToUpdate: [AnyHashable : Any]?](./propertiestoupdate.md)
  A dictionary of property description pairs that describe the updates.
- [var resultType: NSBatchUpdateRequestResultType](./resulttype.md)
  The type of result that Core Data returns from the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/entityname)*