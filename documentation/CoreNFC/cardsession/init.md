# init()

**Framework**: Core NFC  
**Kind**: init

Creates a contactless card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
init() async throws
```

#### Discussion

Creating a card session depends on the following conditions:

- The device is eligible to use a card session.
- The person using the app has accepted the app’s request to use a card session.

> 💡 **Tip**:  Query the [`isSupported`](cardsession/issupported.md) and [`isEligible`](cardsession/iseligible.md) properties before calling this initializer to avoid showing a system card session UI on ineligible devices.

 Query the [`isSupported`](cardsession/issupported.md) and [`isEligible`](cardsession/iseligible.md) properties before calling this initializer to avoid showing a system card session UI on ineligible devices.

This initializer throws an error of type [`CardSession.Error`](cardsession/error.md) if it can’t create a card session. Possible error conditions are:

- [`CardSession.Error.accessNotAccepted`](cardsession/error/accessnotaccepted.md)
- [`CardSession.Error.systemEligibilityFailed`](cardsession/error/systemeligibilityfailed.md)
- [`CardSession.Error.radioDisabled`](cardsession/error/radiodisabled.md)
- [`CardSession.Error.systemNotAvailable`](cardsession/error/systemnotavailable.md)

## See Also

- [CardSession.Error](cardsession/error.md)
  An error type that indicates problems with a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/init())*