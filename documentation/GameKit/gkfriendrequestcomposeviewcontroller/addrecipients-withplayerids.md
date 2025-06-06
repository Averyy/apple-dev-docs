# addRecipients(withPlayerIDs:)

**Framework**: GameKit  
**Kind**: method

Adds recipients based on their Game Center player identifiers.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addRecipients(withPlayerIDs playerIDs: [String])
```

#### Discussion

If you do not add at least once recipient, the recipients field is selected when the view controller is presented so that the player can type a list of recipients.

## Parameters

- `playerIDs`: An array with one or more   objects, each containing an player identifier.

## See Also

- [func addRecipients(withEmailAddresses: [String])](gkfriendrequestcomposeviewcontroller/addrecipients(withemailaddresses:).md)
  Adds recipients based on their email addresses.
- [func addRecipientPlayers([GKPlayer])](gkfriendrequestcomposeviewcontroller/addrecipientplayers(_:).md)
  Adds recipients based on their Game Center player identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/addrecipients(withplayerids:))*