# MTRCommissioningOperation

**Framework**: Matter  
**Kind**: class

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
class MTRCommissioningOperation
```

## Topics

### Initializers
- [init?(parameters: MTRCommissioningParameters, setupPayload: String, delegate: any MTRCommissioningDelegate, queue: dispatch_queue_t)](mtrcommissioningoperation/init(parameters:setuppayload:delegate:queue:).md)
  Prepare to commission a device with the given parameters and the given setup payload (QR code, manual pairing code, etc).  Returns nil if the payload is not valid.
### Instance Properties
- [var matchedPayload: MTRSetupPayload?](mtrcommissioningoperation/matchedpayload.md)
  If not nil, the payload (from possibly multiple payloads represented by the provided setupPayload) that represents the commissionee we successfully established PASE with.  This will only be non-nil after successful PASE establishment.
### Instance Methods
- [func start(with: MTRDeviceController)](mtrcommissioningoperation/start(with:).md)
  Start commissioning with the given controller (which identifies the fabric the commissionee should be commissioned into).  The delegate will be notified if there are any failures.
- [func stop() -> Bool](mtrcommissioningoperation/stop.md)
  Stop commissioning.  This will typically result in commissioning:failedWithError: callbacks to delegates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningoperation)*