# init(smartCard:aid:instanceID:tokenDriver:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a smart card token with the specified smart card, application identifier, and token driver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(smartCard: TKSmartCard, aid AID: Data?, instanceID: String, tokenDriver: TKSmartCardTokenDriver)
```

#### Discussion

This is the designated initializer.

## Parameters

- `smartCard`: The smart card on which the created token should operate.
- `AID`: The ISO 7816-4 application identifier for the smart card.
- `instanceID`: A unique, persistent identifier for this token. This value is typically generated from the serial number of the target hardware.
- `tokenDriver`: The driver associated with the created token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken/init(smartcard:aid:instanceid:tokendriver:))*