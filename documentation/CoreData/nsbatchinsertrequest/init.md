# init()

**Framework**: Core Data  
**Kind**: init

Creates a Core Data batch-insertion request.

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
convenience init()
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init())*