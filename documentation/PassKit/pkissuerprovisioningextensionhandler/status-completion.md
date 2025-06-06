# status(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Reports the status of your Wallet extension.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func status() async -> PKIssuerProvisioningExtensionStatus
```

## Parameters

- `completion`: A completion handler that the system calls to determine if there is a pass available and if adding the pass requires authentication. This handler takes the following parameter:

## See Also

- [class PKIssuerProvisioningExtensionStatus](pkissuerprovisioningextensionstatus.md)
  An object that indicates whether there are any payment cards available to add as Wallet passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionhandler/status(completion:))*