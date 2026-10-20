# status(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Reports the status of your Wallet extension.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func status(completion: @escaping @Sendable (PKIssuerProvisioningExtensionStatus) -> Void)
```

```swift
func status() async -> PKIssuerProvisioningExtensionStatus
```

```objc
- (void) statusWithCompletion:(void (^)(PKIssuerProvisioningExtensionStatus *status)) completion;
```

## Parameters

- `completion`: A completion handler that the system calls to determine if there is a pass available and if adding the pass requires authentication. This handler takes the following parameter:

  - **`status`**: A [`PKIssuerProvisioningExtensionStatus`](../pkissuerprovisioningextensionstatus.md) that indicates whether there are any payment cards available to add as Wallet passes.

## See Also

### Returning extension status
- [class PKIssuerProvisioningExtensionStatus](../pkissuerprovisioningextensionstatus.md)
  An object that indicates whether there are any payment cards available to add as Wallet passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionhandler/status(completion:))*