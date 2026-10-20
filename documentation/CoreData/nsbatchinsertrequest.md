# NSBatchInsertRequest

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSBatchInsertRequest : NSPersistentStoreRequest
```

## Topics

### Creating a Request
- [convenience init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) -> Bool)](./nsbatchinsertrequest/init%28entity,dictionaryhandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) -> Bool)](./nsbatchinsertrequest/init%28entity,managedobjecthandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [convenience init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)](./nsbatchinsertrequest/init%28entityname,dictionaryhandler%29-5l4ps.md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)](./nsbatchinsertrequest/init%28entityname,managedobjecthandler%29-7dr6p.md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [init(entity: NSEntityDescription, objects: [[String : Any]])](./nsbatchinsertrequest/init%28entity,objects%29.md)
  Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [init(entityName: String, objects: [[String : Any]])](./nsbatchinsertrequest/init%28entityname,objects%29.md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [convenience init()](./nsbatchinsertrequest/init%28%29.md)
  Creates a Core Data batch-insertion request.
### Configuring a Request
- [var dictionaryHandler: ((NSMutableDictionary) -> Bool)?](./nsbatchinsertrequest/dictionaryhandler.md)
  A closure that provides a dictionary for your app to insert data into.
- [var entity: NSEntityDescription?](./nsbatchinsertrequest/entity.md)
  The managed entity to insert data into.
- [var entityName: String](./nsbatchinsertrequest/entityname.md)
  The name of the managed entity to insert data into.
- [var managedObjectHandler: ((NSManagedObject) -> Bool)?](./nsbatchinsertrequest/managedobjecthandler.md)
  A closure that provides a managed object for your app to insert data into.
- [var objectsToInsert: [[String : Any]]?](./nsbatchinsertrequest/objectstoinsert.md)
  An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
- [var resultType: NSBatchInsertRequestResultType](./nsbatchinsertrequest/resulttype.md)
  The type of result that Core Data returns from this request.
### Initializers
- [convenience init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)](./nsbatchinsertrequest/init%28entityname,dictionaryhandler%29-74gtn.md)
- [convenience init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)](./nsbatchinsertrequest/init%28entityname,managedobjecthandler%29-2dgkw.md)

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

### Data Inserts
- [class NSBatchInsertResult](./nsbatchinsertresult.md)
  The result that Core Data returns when executing a batch-insertion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest)*