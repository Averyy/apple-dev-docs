# entityDescription(with:)

**Framework**: Core Data  
**Kind**: method

Requests an entity description using the provided context for the managed object type affected by the transaction.

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
class func entityDescription(with context: NSManagedObjectContext) -> NSEntityDescription?
```

#### Return Value

The entity description ([`NSEntityDescription`](nsentitydescription.md)) of the persistent history transaction entity.

## Parameters

- `context`: The managed object context for this request.

## See Also

- [class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?](nspersistenthistorytransaction/fetchrequest.md)
  A fetch request that has the persistent history transaction as the entity.
- [class var entityDescription: NSEntityDescription?](nspersistenthistorytransaction/entitydescription.md)
  The entity description of the persistent history transaction entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/entitydescription(with:))*