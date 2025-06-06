# TKSmartCardTokenDriverDelegate

**Framework**: CryptoTokenKit  
**Kind**: protocol

The interface that a smart card token driver delegate implements to respond to token creation events.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol TKSmartCardTokenDriverDelegate : TKTokenDriverDelegate
```

## Topics

### Delegate Methods
- [func tokenDriver(TKSmartCardTokenDriver, createTokenFor: TKSmartCard, aid: Data?) throws -> TKSmartCardToken](tksmartcardtokendriverdelegate/tokendriver(_:createtokenfor:aid:).md)
  Tells the delegate that a new Smart Card is detected.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [TKTokenDriverDelegate](tktokendriverdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriverdelegate)*