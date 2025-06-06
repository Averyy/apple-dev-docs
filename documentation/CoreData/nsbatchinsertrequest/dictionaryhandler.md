# dictionaryHandler

**Framework**: Core Data  
**Kind**: property

A closure that provides a dictionary for your app to insert data into.

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
var dictionaryHandler: ((NSMutableDictionary) -> Bool)? { get set }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/dictionaryhandler)*