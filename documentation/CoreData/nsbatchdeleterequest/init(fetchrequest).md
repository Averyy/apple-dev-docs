# init(fetchRequest:)

**Framework**: Core Data  
**Kind**: init

Creates a request that deletes the results of the specified fetch request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(fetchRequest fetch: NSFetchRequest<any NSFetchRequestResult>)
```

## Parameters

- `fetch`: The fetch request that identifies the managed objects to delete.

## See Also

- [convenience init(objectIDs: [NSManagedObjectID])](nsbatchdeleterequest/init(objectids:).md)
  Creates a request that deletes the managed objects with the specified identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/init(fetchrequest:))*