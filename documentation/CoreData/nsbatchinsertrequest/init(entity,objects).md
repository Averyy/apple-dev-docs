# init(entity:objects:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.

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
init(entity: NSEntityDescription, objects dictionaries: [[String : Any]])
```

```objc
- (instancetype) initWithEntity:(NSEntityDescription *) entity objects:(NSArray<NSDictionary<NSString *,id> *> *) dictionaries;
```

#### Return Value

A batch-insertion request.

## Parameters

- `entity`: The managed entity to insert data into.
- `dictionaries`: An array of dictionaries that represents objects to insert. Each dictionary contains an attribute name key and a value.

## See Also

### Creating a Request
- [convenience init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) -> Bool)](./init%28entity,dictionaryhandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) -> Bool)](./init%28entity,managedobjecthandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [convenience init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)](./init%28entityname,dictionaryhandler%29-5l4ps.md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)](./init%28entityname,managedobjecthandler%29-7dr6p.md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [init(entityName: String, objects: [[String : Any]])](./init%28entityname,objects%29.md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [convenience init()](./init%28%29.md)
  Creates a Core Data batch-insertion request.
- [+ batchInsertRequestWithEntityName:objects:](./batchinsertrequestwithentityname_objects_.md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entity:objects:))*