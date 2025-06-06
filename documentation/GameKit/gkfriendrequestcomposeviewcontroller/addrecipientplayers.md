# addRecipientPlayers(_:)

**Framework**: GameKit  
**Kind**: method

Adds recipients based on their Game Center player identifiers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addRecipientPlayers(_ players: [GKPlayer])
```

#### Discussion

If you do not add at least once recipient, the recipients field is selected when the view controller is presented so that the player can type a list of recipients. Adding more players than defined by the [`maxNumberOfRecipients()`](gkfriendrequestcomposeviewcontroller/maxnumberofrecipients().md) property causes an exception to be thrown.

## Parameters

- `players`: An array with one or more   objects, each containing an player identifier.

## See Also

- [func addRecipients(withEmailAddresses: [String])](gkfriendrequestcomposeviewcontroller/addrecipients(withemailaddresses:).md)
  Adds recipients based on their email addresses.
- [func addRecipients(withPlayerIDs: [String])](gkfriendrequestcomposeviewcontroller/addrecipients(withplayerids:).md)
  Adds recipients based on their Game Center player identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/addrecipientplayers(_:))*