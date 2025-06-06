# init(identifier:title:art:addRequestConfiguration:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a new entry for a payment pass that a user adds to Wallet.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(identifier: String, title: String, art: CGImage, addRequestConfiguration configuration: PKAddPaymentPassRequestConfiguration)
```

## Parameters

- `identifier`: The value that you use to identify the card.
- `title`: The name for the pass the system displays to the user when they add or select the card.
- `art`: The image that the system displays to the user when they add or select the card.
- `configuration`: The configuration that an   uses to create a secure pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionpaymentpassentry/init(identifier:title:art:addrequestconfiguration:))*