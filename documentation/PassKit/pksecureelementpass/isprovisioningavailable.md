# isProvisioningAvailable

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value indicating whether provisioning is available for this pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var isProvisioningAvailable: Bool { get }
```

#### Discussion

This property is YES when the pass is in a pre-provisioned state and the issuer app can guide the user to complete provisioning. Check this property when passActivationState returns PKSecureElementPassActivationStateDeactivated to determine if provisioning is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/isprovisioningavailable)*