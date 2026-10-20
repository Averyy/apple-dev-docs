# remotePassEntries(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Reports the list of passes available to add to an Apple Watch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func remotePassEntries(completion: @escaping @Sendable ([PKIssuerProvisioningExtensionPassEntry]) -> Void)
```

```swift
func remotePassEntries() async -> [PKIssuerProvisioningExtensionPassEntry]
```

```objc
- (void) remotePassEntriesWithCompletion:(void (^)(NSArray<PKIssuerProvisioningExtensionPassEntry *> *entries)) completion;
```

## Parameters

- `completion`: A completion handler that the system calls to find the list of passes available to add to an Apple Watch. This handler takes the following parameter:

  - **`entries`**: An array [`PKIssuerProvisioningExtensionPassEntry`](../pkissuerprovisioningextensionpassentry.md) items representing the passes that are available to add to Wallet.

## See Also

### Returning available passes
- [func passEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](./passentries%28completion%29.md)
  Reports the list of passes available to add to an iPhone.
- [class PKIssuerProvisioningExtensionPassEntry](../pkissuerprovisioningextensionpassentry.md)
  An object that represents an item available to add to as a Wallet pass.
- [class PKIssuerProvisioningExtensionPaymentPassEntry](../pkissuerprovisioningextensionpaymentpassentry.md)
  An object that represents a payment card available to add as a payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionhandler/remotepassentries(completion:))*