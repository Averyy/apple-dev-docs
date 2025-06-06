# MTRDeviceControllerDelegate

**Framework**: Matter  
**Kind**: protocol

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
protocol MTRDeviceControllerDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?)](mtrdevicecontrollerdelegate/controller(_:commissioningcomplete:).md)
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?, nodeID: NSNumber?)](mtrdevicecontrollerdelegate/controller(_:commissioningcomplete:nodeid:).md)
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?, nodeID: NSNumber?, metrics: MTRMetrics)](mtrdevicecontrollerdelegate/controller(_:commissioningcomplete:nodeid:metrics:).md)
- [func controller(MTRDeviceController, commissioningSessionEstablishmentDone: (any Error)?)](mtrdevicecontrollerdelegate/controller(_:commissioningsessionestablishmentdone:).md)
- [func controller(MTRDeviceController, readCommissioningInfo: MTRProductIdentity)](mtrdevicecontrollerdelegate/controller(_:readcommissioninginfo:).md)
- [func controller(MTRDeviceController, statusUpdate: MTRCommissioningStatus)](mtrdevicecontrollerdelegate/controller(_:statusupdate:).md)
- [func controller(MTRDeviceController, commissioneeHasReceivedNetworkCredentials: NSNumber)](mtrdevicecontrollerdelegate/controller(_:commissioneehasreceivednetworkcredentials:).md)
  Notify the delegate that we have successfully communicated the network credentials to the device being commissioned and are about to tell it to join that network.  Note that for devices that are already on-network this notification will not happen.
- [func controller(MTRDeviceController, read: MTRCommissioneeInfo)](mtrdevicecontrollerdelegate/controller(_:read:).md)
  Notify the delegate when commissioning infomation has been read from the commissionee.
- [func controller(MTRDeviceController, suspendedChangedTo: Bool)](mtrdevicecontrollerdelegate/controller(_:suspendedchangedto:).md)
  Notify the delegate when the suspended state changed of the controller, after this happens the controller will be in the specified state.
- [func devicesChanged(for: MTRDeviceController)](mtrdevicecontrollerdelegate/deviceschanged(for:).md)
  Notify the delegate when the list of MTRDevice objects in memory has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerdelegate)*