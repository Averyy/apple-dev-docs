# controller(_:read:)

**Framework**: Matter  
**Kind**: method

Notify the delegate when commissioning infomation has been read from the commissionee.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
optional func controller(_ controller: MTRDeviceController, read info: MTRCommissioneeInfo)
```

#### Discussion

Note that this notification happens before device attestation is performed, so the information delivered by this notification should not be trusted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerdelegate/controller(_:read:))*