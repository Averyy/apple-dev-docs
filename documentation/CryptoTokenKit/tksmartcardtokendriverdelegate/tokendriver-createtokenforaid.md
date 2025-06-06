# tokenDriver(_:createTokenFor:aid:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that a new Smart Card is detected.

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
func tokenDriver(_ driver: TKSmartCardTokenDriver, createTokenFor smartCard: TKSmartCard, aid AID: Data?) throws -> TKSmartCardToken
```

#### Return Value

The token created for the Smart Card, or `nil` if an error occurs or the delegate decides not to provide a token.

## Parameters

- `driver`: The Smart Card token driver.
- `smartCard`: The detected Smart Card.
- `AID`: The ISO 7816-4 application identifier that is selected on the Smart Card. If the   attributes is not present in the Smart Card token extension property list, no application is selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriverdelegate/tokendriver(_:createtokenfor:aid:))*