# qualityOfService

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The priority that the system uses when it allocates resources to the operations that use this configuration.

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
var qualityOfService: QualityOfService { get set }
```

```objc
@property (assign) NSQualityOfService qualityOfService;
```

## See Also

### Preparing a Configuration
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether operations that use this configuration can send data over the cellular network.
- [var container: CKContainer?](./container.md)
  The configuration’s container.
- [var isLongLived: Bool](./islonglived.md)
  A Boolean value that indicates whether the operations that use this configuration are long-lived.
- [var timeoutIntervalForRequest: TimeInterval](./timeoutintervalforrequest.md)
  The maximum amount of time that a request can take.
- [var timeoutIntervalForResource: TimeInterval](./timeoutintervalforresource.md)
  The maximum amount of time that a resource request can take.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/configuration-swift.class/qualityofservice)*