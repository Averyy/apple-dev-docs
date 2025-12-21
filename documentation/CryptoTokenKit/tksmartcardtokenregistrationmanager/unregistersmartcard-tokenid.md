# unregisterSmartCard(tokenID:)

**Framework**: CryptoTokenKit  
**Kind**: method

Unregisters a smartcard for the provided token ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func unregisterSmartCard(tokenID: String) throws
```

#### Discussion

In case the tokenID is not found, failure is returned.

## Parameters

- `tokenID`: ID of the smartcard


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokenregistrationmanager/unregistersmartcard(tokenid:))*