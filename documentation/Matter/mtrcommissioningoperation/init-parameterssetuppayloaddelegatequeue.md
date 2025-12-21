# init(parameters:setupPayload:delegate:queue:)

**Framework**: Matter  
**Kind**: init

Prepare to commission a device with the given parameters and the given setup payload (QR code, manual pairing code, etc).  Returns nil if the payload is not valid.

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
init?(parameters: MTRCommissioningParameters, setupPayload payload: String, delegate: any MTRCommissioningDelegate, queue: dispatch_queue_t)
```

#### Discussion

The deviceAttestationDelegate property of MTRCommissioningParameters will be ignored. Device attestation notifications will be delivered to the MTRCommissioningDelegate instead.  The failSafeTimeout property of MTRCommissioningParameters will be respected.

The provided delegate will be notified about various things as commissioning proceeds.  The calls into the delegate will happen on the provided queue.

Modifying the parameters after this call will have no effect on the behavior of the MTRCommissioningOperation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningoperation/init(parameters:setuppayload:delegate:queue:))*