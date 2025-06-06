# commissionDevice(in:onboardingPayload:commissioningID:)

**Framework**: MatterSupport  
**Kind**: method

Commissions the device with the onboarding payload.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
func commissionDevice(in home: MatterAddDeviceRequest.Home?, onboardingPayload: String, commissioningID: UUID) async throws
```

## Parameters

- `home`: The selected home for the device.
- `onboardingPayload`: The onboarding payload, as defined by Matter specification, that you need to use to commission the device.
- `commissioningID`: A generated identifier you use with other MatterSupport methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/commissiondevice(in:onboardingpayload:commissioningid:))*