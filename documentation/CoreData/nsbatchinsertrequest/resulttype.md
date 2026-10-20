# resultType

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The type of result that Core Data returns from this request.

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
var resultType: NSBatchInsertRequestResultType { get set }
```

```objc
@property NSBatchInsertRequestResultType resultType;
```

#### Discussion

The default is [`NSBatchInsertRequestResultType.statusOnly`](../nsbatchinsertrequestresulttype/statusonly.md).

## See Also

### Configuring a Request
- [var dictionaryHandler: ((NSMutableDictionary) -> Bool)?](./dictionaryhandler.md)
  A closure that provides a dictionary for your app to insert data into.
- [var entity: NSEntityDescription?](./entity.md)
  The managed entity to insert data into.
- [var entityName: String](./entityname.md)
  The name of the managed entity to insert data into.
- [var managedObjectHandler: ((NSManagedObject) -> Bool)?](./managedobjecthandler.md)
  A closure that provides a managed object for your app to insert data into.
- [var objectsToInsert: [[String : Any]]?](./objectstoinsert.md)
  An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/resulttype)*