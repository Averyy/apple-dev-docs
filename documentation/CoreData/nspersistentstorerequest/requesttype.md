# requestType

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The type of the fetch request.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var requestType: NSPersistentStoreRequestType { get }
```

```objc
@property (readonly) NSPersistentStoreRequestType requestType;
```

## See Also

### Configuring a Request
- [var affectedStores: [NSPersistentStore]?](./affectedstores.md)
  The stores the request should be sent to.
- [enum NSPersistentStoreRequestType](../nspersistentstorerequesttype.md)
  Constants that specify the types of fetch requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorerequest/requesttype)*