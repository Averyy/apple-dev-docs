# registerSmartCard(tokenID:promptMessage:)

**Framework**: CryptoTokenKit  
**Kind**: method

Registers a smartcard with a specific token ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func registerSmartCard(tokenID: String, promptMessage: String) throws
```

#### Discussion

In case the same tokenID is already registered, the registration data are overwritten. In case the smartcard with provided tokenID isn’t found in the system, failure is returned.

## Parameters

- `tokenID`: ID of the smartcard
- `promptMessage`: Message that will be shown in the presented system UI when an operation with this smartcard is requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokenregistrationmanager/registersmartcard(tokenid:promptmessage:))*