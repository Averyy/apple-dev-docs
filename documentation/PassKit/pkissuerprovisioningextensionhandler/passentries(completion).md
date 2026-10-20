# passEntries(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Reports the list of passes available to add to an iPhone.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func passEntries(completion: @escaping @Sendable ([PKIssuerProvisioningExtensionPassEntry]) -> Void)
```

```swift
func passEntries() async -> [PKIssuerProvisioningExtensionPassEntry]
```

```objc
- (void) passEntriesWithCompletion:(void (^)(NSArray<PKIssuerProvisioningExtensionPassEntry *> *entries)) completion;
```

## Parameters

- `completion`: A completion handler that the system calls to find the list of passes available to add to an iPhone. This handler takes the following parameter:

  - **`entries`**: An array [`PKIssuerProvisioningExtensionPassEntry`](../pkissuerprovisioningextensionpassentry.md) items that represents the passes that are available to add to Wallet.

## See Also

### Returning available passes
- [func remotePassEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](./remotepassentries%28completion%29.md)
  Reports the list of passes available to add to an Apple Watch.
- [class PKIssuerProvisioningExtensionPassEntry](../pkissuerprovisioningextensionpassentry.md)
  An object that represents an item available to add to as a Wallet pass.
- [class PKIssuerProvisioningExtensionPaymentPassEntry](../pkissuerprovisioningextensionpaymentpassentry.md)
  An object that represents a payment card available to add as a payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionhandler/passentries(completion:))*