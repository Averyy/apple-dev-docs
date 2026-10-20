# uuid

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The universally unique identifier (UUID) for the HealthKit object that was deleted from the store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (strong, readonly) NSUUID * UUID;
```

#### Discussion

Use this UUID to identify and remove the deleted objects from any copies of the HealthKit data that you have stored outside of HealthKit. For example, if you upload sample data to your server, use the deleted object’s UUID to find and remove it from your server.

## See Also

### Identifying Deleted Objects
- [var metadata: [String : Any]?](./metadata.md)
  The metadata associated with the deleted object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdeletedobject/uuid)*