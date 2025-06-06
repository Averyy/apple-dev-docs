# insertNewObject(forEntityName:into:)

**Framework**: Core Data  
**Kind**: method

Creates, configures, and returns an instance of the class for the entity with a given name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func insertNewObject(forEntityName entityName: String, into context: NSManagedObjectContext) -> NSManagedObject
```

#### Return Value

A new, autoreleased, fully configured instance of the class for the entity named `entityName`. The instance has its entity description set and is inserted it into `context`.

#### Discussion

This method makes it easy for you to create instances of a given entity without worrying about the details of managed object creation. The method is conceptually similar to the following code example.

```objc
NSManagedObjectModel *managedObjectModel =
        [[context persistentStoreCoordinator] managedObjectModel];
NSEntityDescription *entity =
        [[managedObjectModel entitiesByName] objectForKey:entityName];
NSManagedObject *newObject = [[NSManagedObject alloc]
            initWithEntity:entity insertIntoManagedObjectContext:context];
return newObject;
```

## Parameters

- `entityName`: The name of an entity.
- `context`: The managed object context to use.

## See Also

- [init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)](nsmanagedobject/init(entity:insertinto:).md)
  Initializes a managed object from an entity description and inserts it into the specified managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/insertnewobject(forentityname:into:))*