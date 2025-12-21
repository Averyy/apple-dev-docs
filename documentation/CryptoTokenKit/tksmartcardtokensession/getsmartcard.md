# getSmartCard()

**Framework**: CryptoTokenKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func getSmartCard() throws -> TKSmartCard
```

#### Discussion

Returns a TKSmartCard instance with an active exclusive session and the SmartCard application selected. Replaces the deprecated @c smartCard property.

The TKSmartCard object is only accessible within the methods of the TKTokenSessionDelegate protocol. If the associated token has an AID set, the returned card will have an exclusive session already opened and the specified application selected. In this scenario: Do not call -[TKSmartCard beginSessionWithReply:]) on the returned SmartCard instance. The system manages the session lifecycle and will terminate it automatically when the current token request servicing is finished. Do not call -[TKSmartCard endSession]. You can use the `smartCard.context` property to store any context-specific state information related to the card. This property is automatically set to `nil` if the card is reset or accessed by a different TKSmartCard instance (potentially in another process). Before performing an operation, check the `TKSmartCard.context` property for a previously stored value. This can help you avoid potentially costly restoration of the SmartCard state if it’s already available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession/getsmartcard())*