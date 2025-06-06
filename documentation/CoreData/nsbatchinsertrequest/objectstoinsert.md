# objectsToInsert

**Framework**: Core Data  
**Kind**: property

An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.

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
var objectsToInsert: [[String : Any]]? { get set }
```

## See Also

- [var dictionaryHandler: ((NSMutableDictionary) -> Bool)?](nsbatchinsertrequest/dictionaryhandler.md)
  A closure that provides a dictionary for your app to insert data into.
- [var entity: NSEntityDescription?](nsbatchinsertrequest/entity.md)
  The managed entity to insert data into.
- [var entityName: String](nsbatchinsertrequest/entityname.md)
  The name of the managed entity to insert data into.
- [var managedObjectHandler: ((NSManagedObject) -> Bool)?](nsbatchinsertrequest/managedobjecthandler.md)
  A closure that provides a managed object for your app to insert data into.
- [var resultType: NSBatchInsertRequestResultType](nsbatchinsertrequest/resulttype.md)
  The type of result that Core Data returns from this request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/objectstoinsert)*