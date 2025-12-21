# MTRCommissioningDelegate

**Framework**: Matter  
**Kind**: protocol

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
protocol MTRCommissioningDelegate : NSObjectProtocol
```

## Topics

### Instance Methods
- [func commissioning(MTRCommissioningOperation, completedDeviceAttestation: MTRDeviceAttestationDeviceInfo, error: (any Error)?, completion: () -> Void)](mtrcommissioningdelegate/commissioning(_:completeddeviceattestation:error:completion:).md)
  Notification that device attestation has completed.
- [func commissioning(MTRCommissioningOperation, failedWithError: any Error, metrics: MTRMetrics)](mtrcommissioningdelegate/commissioning(_:failedwitherror:metrics:).md)
  Notification that commissioning has failed.
- [func commissioning(MTRCommissioningOperation, needsThreadCredentialsWithScanResults: [MTRNetworkCommissioningClusterThreadInterfaceScanResultStruct]?, error: (any Error)?, completion: (Data) -> Void)](mtrcommissioningdelegate/commissioning(_:needsthreadcredentialswithscanresults:error:completion:).md)
  Callback that gets called for a commissionee that supports Thread if Thread network commissioning is required and an operational dataset was not provided in MTRCommissioningParameters.
- [func commissioning(MTRCommissioningOperation, needsWiFiCredentialsWithScanResults: [MTRNetworkCommissioningClusterWiFiInterfaceScanResultStruct]?, error: (any Error)?, completion: (Data, Data?) -> Void)](mtrcommissioningdelegate/commissioning(_:needswificredentialswithscanresults:error:completion:).md)
  Callback that gets called for a commissionee that supports Wi-Fi if Wi-Fi network commissioning is required and Wi-Fi credentials were not provided in MTRCommissioningParameters.
- [func commissioning(MTRCommissioningOperation, read: MTRCommissioneeInfo)](mtrcommissioningdelegate/commissioning(_:read:).md)
  Callback that gets called after various information (product identity, optionally endpoint structure information, optionally other attributes that were requested) has been read from the commissionee.
- [func commissioning(MTRCommissioningOperation, succeededForNodeID: NSNumber, metrics: MTRMetrics)](mtrcommissioningdelegate/commissioning(_:succeededfornodeid:metrics:).md)
  Notification that commissioning has succeeded.
- [func commissioningProvisionedNetworkCredentials(MTRCommissioningOperation)](mtrcommissioningdelegate/commissioningprovisionednetworkcredentials(_:).md)
  Notification that network credentials have been successfully communicated to the commissionee and it’s going to try to join that network.  Note that for commissionees that are already on-network this notification will not happen.
- [func commissioningStartingNetworkScan(MTRCommissioningOperation)](mtrcommissioningdelegate/commissioningstartingnetworkscan(_:).md)
  Notification that a network scan is starting.  This will only happen if a network scan is performed during commissioning.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate)*