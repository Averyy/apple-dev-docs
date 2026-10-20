# MTRDeviceControllerDelegate

**Framework**: Matter  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTRDeviceControllerDelegate <NSObject>
```

## Topics

### Instance Methods
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?)](./mtrdevicecontrollerdelegate/controller%28_,commissioningcomplete%29.md)
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?, nodeID: NSNumber?)](./mtrdevicecontrollerdelegate/controller%28_,commissioningcomplete,nodeid%29.md)
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?, nodeID: NSNumber?, metrics: MTRMetrics)](./mtrdevicecontrollerdelegate/controller%28_,commissioningcomplete,nodeid,metrics%29.md)
- [func controller(MTRDeviceController, commissioningSessionEstablishmentDone: (any Error)?)](./mtrdevicecontrollerdelegate/controller%28_,commissioningsessionestablishmentdone%29.md)
- [func controller(MTRDeviceController, readCommissioningInfo: MTRProductIdentity)](./mtrdevicecontrollerdelegate/controller%28_,readcommissioninginfo%29.md)
- [func controller(MTRDeviceController, statusUpdate: MTRCommissioningStatus)](./mtrdevicecontrollerdelegate/controller%28_,statusupdate%29.md)
- [func controller(MTRDeviceController, commissioneeHasReceivedNetworkCredentials: NSNumber)](./mtrdevicecontrollerdelegate/controller%28_,commissioneehasreceivednetworkcredentials%29.md)
  Notify the delegate that we have successfully communicated the network credentials to the device being commissioned and are about to tell it to join that network.  Note that for devices that are already on-network this notification will not happen.
- [func controller(MTRDeviceController, commissioningComplete: (any Error)?, nodeID: NSNumber?, metrics: MTRMetrics, context: [String : Any])](./mtrdevicecontrollerdelegate/controller%28_,commissioningcomplete,nodeid,metrics,context%29.md)
  Notify the delegate when commissioning is completed.
- [func controller(MTRDeviceController, read: MTRCommissioneeInfo)](./mtrdevicecontrollerdelegate/controller%28_,read%29.md)
  Notify the delegate when commissioning infomation has been read from the commissionee.
- [func controller(MTRDeviceController, suspendedChangedTo: Bool)](./mtrdevicecontrollerdelegate/controller%28_,suspendedchangedto%29.md)
  Notify the delegate when the suspended state changed of the controller, after this happens the controller will be in the specified state.
- [func devicesChanged(for: MTRDeviceController)](./mtrdevicecontrollerdelegate/deviceschanged%28for%29.md)
  Notify the delegate when the list of MTRDevice objects in memory has changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerdelegate)*