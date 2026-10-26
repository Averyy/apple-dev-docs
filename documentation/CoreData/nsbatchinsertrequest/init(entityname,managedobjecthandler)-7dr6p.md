# init(entityName:managedObjectHandler:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(entityName: String, managedObjectHandler handler: @escaping (NSManagedObject) -> Bool)
```

```objc
+ (instancetype) batchInsertRequestWithEntityName:(NSString *) entityName managedObjectHandler:(BOOL (^)(NSManagedObject *obj)) handler;
```

#### Return Value

A batch-insertion request.

#### Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then finishes the request and saves the data.

## Parameters

- `entityName`: The name of the managed entity that defines the object to create.
- `handler`: A closure that inserts data into the managed entity.

## See Also

### Creating a Request
- [convenience init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) -> Bool)](./init%28entity,dictionaryhandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) -> Bool)](./init%28entity,managedobjecthandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [convenience init(entityName: String, dictionaryHandler: (NSMutableDictionary) -> Bool)](./init%28entityname,dictionaryhandler%29-5l4ps.md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [init(entity: NSEntityDescription, objects: [[String : Any]])](./init%28entity,objects%29.md)
  Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [init(entityName: String, objects: [[String : Any]])](./init%28entityname,objects%29.md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [convenience init()](./init%28%29.md)
  Creates a Core Data batch-insertion request.
- [+ batchInsertRequestWithEntityName:objects:](./batchinsertrequestwithentityname_objects_.md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entityname:managedobjecthandler:)-7dr6p)*