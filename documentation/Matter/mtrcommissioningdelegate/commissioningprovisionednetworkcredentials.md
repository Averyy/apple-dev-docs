# commissioningProvisionedNetworkCredentials(_:)

**Framework**: Matter  
**Kind**: method

Notification that network credentials have been successfully communicated to the commissionee and it’s going to try to join that network.  Note that for commissionees that are already on-network this notification will not happen.

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
optional func commissioningProvisionedNetworkCredentials(_ commissioning: MTRCommissioningOperation)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioningprovisionednetworkcredentials(_:))*