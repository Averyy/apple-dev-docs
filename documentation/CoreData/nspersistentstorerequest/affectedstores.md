# affectedStores

**Framework**: Core Data  
**Kind**: property

The stores the request should be sent to.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var affectedStores: [NSPersistentStore]? { get set }
```

#### Discussion

The array contains instances of [`NSPersistentStore`](nspersistentstore.md).

## See Also

- [Core Data Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [var requestType: NSPersistentStoreRequestType](nspersistentstorerequest/requesttype.md)
  The type of the fetch request.
- [enum NSPersistentStoreRequestType](nspersistentstorerequesttype.md)
  Constants that specify the types of fetch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/affectedstores)*