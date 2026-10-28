# entityDescription

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

The entity description of the persistent history transaction entity.

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
class var entityDescription: NSEntityDescription? { get }
```

```objc
@property (class, readonly, nullable) NSEntityDescription * entityDescription;
```

## Discussion

The entity description of [`NSPersistentHistoryTransaction`](../nspersistenthistorytransaction.md) lists the properties of the persistent history change. This can be useful for filtering your request.

## See Also

### Customizing History Fetch Requests
- [class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?](./fetchrequest.md)
  A fetch request that has the persistent history transaction as the entity.
- [class func entityDescription(with: NSManagedObjectContext) -> NSEntityDescription?](./entitydescription%28with%29.md)
  Requests an entity description using the provided context for the managed object type affected by the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/entitydescription)*