# init(objectIDs:)

**Framework**: Core Data  
**Kind**: init

Creates a request that deletes the managed objects with the specified identifiers.

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
convenience init(objectIDs objects: [NSManagedObjectID])
```

#### Discussion

> ❗ **Important**:  The identifiers your provide must be from managed objects of the same entity type; mixing entity types results in an error when you execute the request.

## Parameters

- `objects`: The array that contains the identifiers of the managed objects to delete.

## See Also

- [init(fetchRequest: NSFetchRequest<any NSFetchRequestResult>)](nsbatchdeleterequest/init(fetchrequest:).md)
  Creates a request that deletes the results of the specified fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/init(objectids:))*