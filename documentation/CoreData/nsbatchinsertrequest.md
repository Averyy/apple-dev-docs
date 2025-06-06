# NSBatchInsertRequest

**Framework**: Core Data  
**Kind**: class

A request to insert a batch of data in a persistent store.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class NSBatchInsertRequest
```

## Topics

### Creating a Request
- [convenience init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) -> Bool)](nsbatchinsertrequest/init(entity:dictionaryhandler:).md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) -> Bool)](nsbatchinsertrequest/init(entity:managedobjecthandler:).md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [convenience init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)](nsbatchinsertrequest/init(entityname:dictionaryhandler:).md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)](nsbatchinsertrequest/init(entityname:managedobjecthandler:).md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [init(entity: NSEntityDescription, objects: [[String : Any]])](nsbatchinsertrequest/init(entity:objects:).md)
  Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [init(entityName: String, objects: [[String : Any]])](nsbatchinsertrequest/init(entityname:objects:).md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [convenience init()](nsbatchinsertrequest/init.md)
  Creates a Core Data batch-insertion request.
### Configuring a Request
- [var dictionaryHandler: ((NSMutableDictionary) -> Bool)?](nsbatchinsertrequest/dictionaryhandler.md)
  A closure that provides a dictionary for your app to insert data into.
- [var entity: NSEntityDescription?](nsbatchinsertrequest/entity.md)
  The managed entity to insert data into.
- [var entityName: String](nsbatchinsertrequest/entityname.md)
  The name of the managed entity to insert data into.
- [var managedObjectHandler: ((NSManagedObject) -> Bool)?](nsbatchinsertrequest/managedobjecthandler.md)
  A closure that provides a managed object for your app to insert data into.
- [var objectsToInsert: [[String : Any]]?](nsbatchinsertrequest/objectstoinsert.md)
  An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
- [var resultType: NSBatchInsertRequestResultType](nsbatchinsertrequest/resulttype.md)
  The type of result that Core Data returns from this request.

## Relationships

### Inherits From
- [NSPersistentStoreRequest](nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSBatchInsertResult](nsbatchinsertresult.md)
  The result that Core Data returns when executing a batch-insertion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest)*