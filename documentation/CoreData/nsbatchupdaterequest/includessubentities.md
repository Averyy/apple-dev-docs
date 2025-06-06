# includesSubentities

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether to update subentities.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var includesSubentities: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var entity: NSEntityDescription](nsbatchupdaterequest/entity.md)
  The managed entity to update data for.
- [var entityName: String](nsbatchupdaterequest/entityname.md)
  The name of the managed entity to update data for.
- [var predicate: NSPredicate?](nsbatchupdaterequest/predicate.md)
  A predicate that identifies the objects to update.
- [var propertiesToUpdate: [AnyHashable : Any]?](nsbatchupdaterequest/propertiestoupdate.md)
  A dictionary of property description pairs that describe the updates.
- [var resultType: NSBatchUpdateRequestResultType](nsbatchupdaterequest/resulttype.md)
  The type of result that Core Data returns from the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/includessubentities)*