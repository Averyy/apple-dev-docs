# fetchRequest

**Framework**: Core Data  
**Kind**: property

The fetch request that identifies the managed objects to delete.

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
@NSCopying
var fetchRequest: NSFetchRequest<any NSFetchRequestResult> { get }
```

#### Discussion

This property contains the fetch request that identifies the managed objects to delete. If you initialize `NSBatchDeleteRequest` with an array of [`NSManagedObjectID`](nsmanagedobjectid.md), Core Data automatically generates a fetch request with a predicate that matches the identifiers in that array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/fetchrequest)*