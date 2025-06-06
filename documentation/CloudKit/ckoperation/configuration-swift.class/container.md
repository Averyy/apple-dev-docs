# container

**Framework**: CloudKit  
**Kind**: property

The configuration’s container.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var container: CKContainer? { get set }
```

#### Discussion

If you don’t provide a container, CloudKit uses the default container that [`CKContainer`](ckcontainer.md) provides.

## See Also

- [var allowsCellularAccess: Bool](ckoperation/configuration-swift.class/allowscellularaccess.md)
  A Boolean value that indicates whether operations that use this configuration can send data over the cellular network.
- [var isLongLived: Bool](ckoperation/configuration-swift.class/islonglived.md)
  A Boolean value that indicates whether the operations that use this configuration are long-lived.
- [var qualityOfService: QualityOfService](ckoperation/configuration-swift.class/qualityofservice.md)
  The priority that the system uses when it allocates resources to the operations that use this configuration.
- [var timeoutIntervalForRequest: TimeInterval](ckoperation/configuration-swift.class/timeoutintervalforrequest.md)
  The maximum amount of time that a request can take.
- [var timeoutIntervalForResource: TimeInterval](ckoperation/configuration-swift.class/timeoutintervalforresource.md)
  The maximum amount of time that a resource request can take.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/configuration-swift.class/container)*