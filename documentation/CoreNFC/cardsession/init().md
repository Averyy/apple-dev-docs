# init()

**Framework**: Core NFC  
**Kind**: init  
**Role**: Initializer

Creates a contactless card session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
init() async throws
```

#### Discussion

Creating a card session depends on the following conditions:

- The device is eligible to use a card session.
- The person using the app has accepted the app’s request to use a card session.

> 💡 **Tip**:  Query the [`isSupported`](./issupported.md) and [`isEligible`](./iseligible.md) properties before calling this initializer to avoid showing a system card session UI on ineligible devices.

This initializer throws an error of type [`CardSession.Error`](./error.md) if it can’t create a card session. Possible error conditions are:

- [`CardSession.Error.accessNotAccepted`](./error/accessnotaccepted.md)
- [`CardSession.Error.systemEligibilityFailed`](./error/systemeligibilityfailed.md)
- [`CardSession.Error.radioDisabled`](./error/radiodisabled.md)
- [`CardSession.Error.systemNotAvailable`](./error/systemnotavailable.md)

## See Also

### Creating a card session
- [CardSession.Error](./error.md)
  An error type that indicates problems with a card session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/init())*