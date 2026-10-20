# init(entityName:dictionaryHandler:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(entityName: String, dictionaryHandler handler: @escaping (NSMutableDictionary) -> Bool)
```

```objc
+ (instancetype) batchInsertRequestWithEntityName:(NSString *) entityName dictionaryHandler:(BOOL (^)(NSMutableDictionary<NSString *,id> *obj)) handler;
```

#### Return Value

A batch-insertion request.

#### Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then finishes the request and saves the data.

## Parameters

- `entityName`: The name of the managed entity to insert data into.
- `handler`: A closure that provides a dictionary that represents an object to insert. The dictionary contains an attribute name key and a value.

## See Also

### Creating a Request
- [convenience init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) -> Bool)](./init%28entity,dictionaryhandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [convenience init(entity: NSEntityDescription, managedObjectHandler: (NSManagedObject) -> Bool)](./init%28entity,managedobjecthandler%29.md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [convenience init(entityName: String, managedObjectHandler: (NSManagedObject) -> Bool)](./init%28entityname,managedobjecthandler%29-7dr6p.md)
  Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [init(entity: NSEntityDescription, objects: [[String : Any]])](./init%28entity,objects%29.md)
  Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [init(entityName: String, objects: [[String : Any]])](./init%28entityname,objects%29.md)
  Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [convenience init()](./init%28%29.md)
  Creates a Core Data batch-insertion request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entityname:dictionaryhandler:)-5l4ps)*