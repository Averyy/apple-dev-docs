# customerConfiguration

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

A structure containing configuration information of the customer device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final var customerConfiguration: CustomerEngagementSession.CustomerConfiguration? { get }
```

## Discussion

The value is available after the [`CustomerEngagementSession.Event.ready`](./event/ready.md) event.

## See Also

### Getting customer configuration
- [CustomerEngagementSession.CustomerConfiguration](./customerconfiguration-swift.struct.md)
  A structure that contains configuration details for the connected customer device.
- [CustomerEngagementSession.PeerClientType](./peerclienttype.md)
  A value that indicates the type of connected peer client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/customerconfiguration-swift.property)*