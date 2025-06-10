# NFCPresentmentIntentAssertion

**Framework**: Core NFC  
**Kind**: class

An object that signals your app’s intention to make exclusive use of the device’s contactless features.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
final class NFCPresentmentIntentAssertion
```

#### Overview

Acquire an instance of this class to prevent the system default contactless app from launching in response to a user gesture or NFC reader RF field. You do this when the person using your app expresses an active intent to perform an NFC transaction, like choosing a credential such as a payment card or transit pass. You can only acquire a [`NFCPresentmentIntentAssertion`](nfcpresentmentintentassertion.md) when your app is in the foreground state.

The presentment intent assertion expires if any of the following occur:

- The presentment intent assertion object deinitializes.
- Your app goes into the background.
- 15 seconds elapse.

After the presentment intent assertion expires, you must wait through a 15-second cool-down period before you can acquire a new instance.

## Topics

### Acquiring a presentment intention instance
- [static func acquire() async throws -> NFCPresentmentIntentAssertion](nfcpresentmentintentassertion/acquire.md)
  Acquire a presentment intent assertion instance from the system.
### Testing presentment intention validity
- [var isValid: Bool](nfcpresentmentintentassertion/isvalid.md)
  A Boolean property that indicates whether the presentment intent assertion instance is still valid.
- [NFCPresentmentIntentAssertion.Error](nfcpresentmentintentassertion/error.md)
  An error type that indicates problems with the presentment intent assertion.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CardSession](cardsession.md)
  An ISO 7816 card emulation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion)*