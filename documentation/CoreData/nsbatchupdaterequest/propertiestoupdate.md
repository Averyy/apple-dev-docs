# propertiesToUpdate

**Framework**: Core Data  
**Kind**: property

A dictionary of property description pairs that describe the updates.

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
var propertiesToUpdate: [AnyHashable : Any]? { get set }
```

#### Discussion

The dictionary keys are either [`NSPropertyDescription`](nspropertydescription.md) objects or strings that identify the property name.

The dictionary values are either a constant value or an [`NSExpression`](https://developer.apple.com/documentation/Foundation/NSExpression) that evaluates to a scalar value.

## See Also

- [var entity: NSEntityDescription](nsbatchupdaterequest/entity.md)
  The managed entity to update data for.
- [var entityName: String](nsbatchupdaterequest/entityname.md)
  The name of the managed entity to update data for.
- [var includesSubentities: Bool](nsbatchupdaterequest/includessubentities.md)
  A Boolean value that indicates whether to update subentities.
- [var predicate: NSPredicate?](nsbatchupdaterequest/predicate.md)
  A predicate that identifies the objects to update.
- [var resultType: NSBatchUpdateRequestResultType](nsbatchupdaterequest/resulttype.md)
  The type of result that Core Data returns from the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/propertiestoupdate)*