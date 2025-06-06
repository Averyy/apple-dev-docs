# init(entity:managedObjectHandler:)

**Framework**: Core Data  
**Kind**: init

Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(entity: NSEntityDescription, managedObjectHandler handler: @escaping (NSManagedObject) -> Bool)
```

#### Return Value

A batch-insertion request.

#### Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then finishes the request and saves the data.

## Parameters

- `entity`: A managed entity to insert data into.
- `handler`: A closure that inserts data into the managed entity.

## See Also

- [convenience init(entity: NSEntityDescription, dictionaryHandler: (NSMutableDictionary) -> Bool)](nsbatchinsertrequest/init(entity:dictionaryhandler:).md)
  Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entity:managedobjecthandler:))*