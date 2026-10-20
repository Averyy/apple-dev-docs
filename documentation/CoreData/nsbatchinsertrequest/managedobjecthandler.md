# managedObjectHandler

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A closure that provides a managed object for your app to insert data into.

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
var managedObjectHandler: ((NSManagedObject) -> Bool)? { get set }
```

```objc
@property (copy, nullable) BOOL (^managedObjectHandler)(NSManagedObject *obj);
```

## See Also

### Configuring a Request
- [var dictionaryHandler: ((NSMutableDictionary) -> Bool)?](./dictionaryhandler.md)
  A closure that provides a dictionary for your app to insert data into.
- [var entity: NSEntityDescription?](./entity.md)
  The managed entity to insert data into.
- [var entityName: String](./entityname.md)
  The name of the managed entity to insert data into.
- [var objectsToInsert: [[String : Any]]?](./objectstoinsert.md)
  An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
- [var resultType: NSBatchInsertRequestResultType](./resulttype.md)
  The type of result that Core Data returns from this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/managedobjecthandler)*