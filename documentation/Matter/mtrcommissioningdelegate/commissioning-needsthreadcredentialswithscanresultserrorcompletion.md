# commissioning(_:needsThreadCredentialsWithScanResults:error:completion:)

**Framework**: Matter  
**Kind**: method

Callback that gets called for a commissionee that supports Thread if Thread network commissioning is required and an operational dataset was not provided in MTRCommissioningParameters.

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
optional func commissioning(_ commissioning: MTRCommissioningOperation, needsThreadCredentialsWithScanResults networks: [MTRNetworkCommissioningClusterThreadInterfaceScanResultStruct]?, error: (any Error)?) async -> Data
```

#### Discussion

Commissioning will pause, including in cases when the network scan failed, until the completion is invoked with the operational dataset the commissionee should use, or until commissioning is stopped.

- error will be non-nil if a scan was attempted and failed.
- networks will be non-nil if a scan was attempted and succeeded.
- Both error and networks will be nil if no scan was performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate/commissioning(_:needsthreadcredentialswithscanresults:error:completion:))*