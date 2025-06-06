# passEntries(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Reports the list of passes available to add to an iPhone.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func passEntries() async -> [PKIssuerProvisioningExtensionPassEntry]
```

## Parameters

- `completion`: A completion handler that the system calls to find the list of passes available to add to an iPhone. This handler takes the following parameter:

## See Also

- [func remotePassEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](pkissuerprovisioningextensionhandler/remotepassentries(completion:).md)
  Reports the list of passes available to add to an Apple Watch.
- [class PKIssuerProvisioningExtensionPassEntry](pkissuerprovisioningextensionpassentry.md)
  An object that represents an item available to add to as a Wallet pass.
- [class PKIssuerProvisioningExtensionPaymentPassEntry](pkissuerprovisioningextensionpaymentpassentry.md)
  An object that represents a payment card available to add as a payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionhandler/passentries(completion:))*