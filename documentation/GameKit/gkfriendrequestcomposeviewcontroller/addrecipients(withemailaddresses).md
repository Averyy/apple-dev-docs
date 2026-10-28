# addRecipients(withEmailAddresses:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Adds recipients based on their email addresses.

**Availability**:
- iOS 4.2+ - Deprecated in 10.0
- iPadOS 4.2+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func addRecipients(withEmailAddresses emailAddresses: [String])
```

```objc
- (void) addRecipientsWithEmailAddresses:(NSArray<NSString *> *) emailAddresses;
```

## Discussion

If you do not add at least once recipient, the recipients field is selected when the view controller is presented so that the player can type a list of recipients. Adding more players than defined by the [`maxNumberOfRecipients()`](./maxnumberofrecipients%28%29.md) property causes an exception to be thrown.

## Parameters

- `emailAddresses`: An array with one or more [`NSString`](../../Foundation/nsstring.md) objects, each containing an email address.

## See Also

### Adding Recipients
- [func addRecipientPlayers([GKPlayer])](./addrecipientplayers%28_%29.md)
  Adds recipients based on their Game Center player identifiers.
- [func addRecipients(withPlayerIDs: [String])](./addrecipients%28withplayerids%29.md)
  Adds recipients based on their Game Center player identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/addrecipients(withemailaddresses:))*