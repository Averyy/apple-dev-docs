# NSPersistentStoreRequestType

**Framework**: Core Data  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the types of fetch requests.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum NSPersistentStoreRequestType
```

```c
enum NSPersistentStoreRequestType : NSUInteger;
```

#### Overview

[`requestType`](./nspersistentstorerequest/requesttype.md) uses these constants.

## Topics

### Constants
- [NSPersistentStoreRequestType.fetchRequestType](./nspersistentstorerequesttype/fetchrequesttype.md)
  Specifies that the request returns managed objects.
- [NSPersistentStoreRequestType.saveRequestType](./nspersistentstorerequesttype/saverequesttype.md)
  Specifies that the request saves managed objects.
- [NSPersistentStoreRequestType.batchInsertRequestType](./nspersistentstorerequesttype/batchinsertrequesttype.md)
  A request that inserts data into a persistent store using a batch of managed objects or dictionaries.
- [NSPersistentStoreRequestType.batchUpdateRequestType](./nspersistentstorerequesttype/batchupdaterequesttype.md)
  A request that updates data for multiple managed objects in a persistent store.
- [NSPersistentStoreRequestType.batchDeleteRequestType](./nspersistentstorerequesttype/batchdeleterequesttype.md)
  A request that deletes data for multiple managed objects from a persistent store.
### Initializers
- [init?(rawValue: UInt)](./nspersistentstorerequesttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a Request
- [var affectedStores: [NSPersistentStore]?](./nspersistentstorerequest/affectedstores.md)
  The stores the request should be sent to.
- [var requestType: NSPersistentStoreRequestType](./nspersistentstorerequest/requesttype.md)
  The type of the fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorerequesttype)*