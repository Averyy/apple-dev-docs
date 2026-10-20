# NSBatchUpdateRequest

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

A request to Core Data to do a batch update of data in a persistent store without loading any data into memory.

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
class NSBatchUpdateRequest
```

```objc
@interface NSBatchUpdateRequest : NSPersistentStoreRequest
```

## Topics

### Creating a Request
- [init(entity: NSEntityDescription)](./nsbatchupdaterequest/init%28entity%29.md)
  Creates a batch-update request for a managed entity.
- [init(entityName: String)](./nsbatchupdaterequest/init%28entityname%29.md)
  Creates a batch-update request for a named managed entity.
### Configuring a Request
- [var entity: NSEntityDescription](./nsbatchupdaterequest/entity.md)
  The managed entity to update data for.
- [var entityName: String](./nsbatchupdaterequest/entityname.md)
  The name of the managed entity to update data for.
- [var includesSubentities: Bool](./nsbatchupdaterequest/includessubentities.md)
  A Boolean value that indicates whether to update subentities.
- [var predicate: NSPredicate?](./nsbatchupdaterequest/predicate.md)
  A predicate that identifies the objects to update.
- [var propertiesToUpdate: [AnyHashable : Any]?](./nsbatchupdaterequest/propertiestoupdate.md)
  A dictionary of property description pairs that describe the updates.
- [var resultType: NSBatchUpdateRequestResultType](./nsbatchupdaterequest/resulttype.md)
  The type of result that Core Data returns from the request.

## Relationships

### Inherits From
- [NSPersistentStoreRequest](./nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data Updates
- [class NSBatchUpdateResult](./nsbatchupdateresult.md)
  The result returned when executing a batch update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest)*