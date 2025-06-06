# addRecipients(withEmailAddresses:)

**Framework**: GameKit  
**Kind**: method

Adds recipients based on their email addresses.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addRecipients(withEmailAddresses emailAddresses: [String])
```

#### Discussion

If you do not add at least once recipient, the recipients field is selected when the view controller is presented so that the player can type a list of recipients. Adding more players than defined by the [`maxNumberOfRecipients()`](gkfriendrequestcomposeviewcontroller/maxnumberofrecipients().md) property causes an exception to be thrown.

## Parameters

- `emailAddresses`: An array with one or more   objects, each containing an email address.

## See Also

- [func addRecipientPlayers([GKPlayer])](gkfriendrequestcomposeviewcontroller/addrecipientplayers(_:).md)
  Adds recipients based on their Game Center player identifiers.
- [func addRecipients(withPlayerIDs: [String])](gkfriendrequestcomposeviewcontroller/addrecipients(withplayerids:).md)
  Adds recipients based on their Game Center player identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/addrecipients(withemailaddresses:))*