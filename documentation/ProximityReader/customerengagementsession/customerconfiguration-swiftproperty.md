# customerConfiguration

**Framework**: ProximityReader  
**Kind**: property

A structure containing configuration information of the customer device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var customerConfiguration: CustomerEngagementSession.CustomerConfiguration? { get }
```

#### Discussion

The value is available after the [`CustomerEngagementSession.Event.ready`](customerengagementsession/event/ready.md) event.

## See Also

- [CustomerEngagementSession.CustomerConfiguration](customerengagementsession/customerconfiguration-swift.struct.md)
  A structure that contains configuration details for the connected customer device.
- [CustomerEngagementSession.PeerClientType](customerengagementsession/peerclienttype.md)
  A value that indicates the type of connected peer client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/customerconfiguration-swift.property)*