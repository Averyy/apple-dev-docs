# smartCard

**Framework**: CryptoTokenKit  
**Kind**: property

The smart card for the active exclusive session and selected application.

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
var smartCard: TKSmartCard { get }
```

#### Discussion

This property can only be accessed in the implementation of a `TKTokenSessionDelegate` protocol delegate method. If the associated token has a value set for the [`aid`](tksmartcardtoken/aid.md) property, this property opens an exclusive session to the card, with the application already selected.

You should not call [`beginSession(reply:)`](tksmartcard/beginsession(reply:).md) or [`endSession()`](tksmartcard/endsession().md) on the returned value. Instead, the system will take care of beginning the exclusive session and terminating it when the current token request servicing is finished.

You can store any kind of information representing state of the card using the [`context`](tksmartcard/context.md) property. This property will be automatically set to `nil` if the card is reset or accessed by different [`TKSmartCard`](tksmartcard.md) instance, such as by another process. You can check the [`context`](tksmartcard/context.md) property for any previously stored values as a way to avoid costly state restoration before performing an operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession/smartcard)*