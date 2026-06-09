# isProvisioningAvailable

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value indicating whether provisioning is available for this pass.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var isProvisioningAvailable: Bool { get }
```

#### Discussion

This property is YES when the pass is in a pre-provisioned state and the issuer app can guide the user to complete provisioning. Check this property when passActivationState returns PKSecureElementPassActivationStateDeactivated to determine if provisioning is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/isprovisioningavailable)*