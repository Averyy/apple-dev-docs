# controller(_:commissioningComplete:nodeID:metrics:context:)

**Framework**: Matter  
**Kind**: method

Notify the delegate when commissioning is completed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
optional func controller(_ controller: MTRDeviceController, commissioningComplete error: (any Error)?, nodeID: NSNumber?, metrics: MTRMetrics, context: [String : Any])
```

#### Discussion

Exactly one of error and nodeID will be nil.

If nodeID is not nil, then it represents the node id the node was assigned, as encoded in its operational certificate.

The metrics object contains information corresponding to the commissioning session.

The context parameter is a dictionary. See MTRCommissioningDelegate’s commissioning:succeededForNodeID:metrics:context for the supported keys.

If supported, this selector will be used in preference to controller:commissioningComplete:nodeID: and controller:commissioningComplete:nodeID:metrics:.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerdelegate/controller(_:commissioningcomplete:nodeid:metrics:context:))*