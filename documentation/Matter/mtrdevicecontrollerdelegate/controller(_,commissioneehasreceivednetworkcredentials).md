# controller(_:commissioneeHasReceivedNetworkCredentials:)

**Framework**: Matter  
**Kind**: method

Notify the delegate that we have successfully communicated the network credentials to the device being commissioned and are about to tell it to join that network.  Note that for devices that are already on-network this notification will not happen.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
optional func controller(_ controller: MTRDeviceController, commissioneeHasReceivedNetworkCredentials nodeID: NSNumber)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerdelegate/controller(_:commissioneehasreceivednetworkcredentials:))*