# addRecipientPlayers(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Adds recipients based on their Game Center player identifiers.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func addRecipientPlayers(_ players: [GKPlayer])
```

```objc
- (void) addRecipientPlayers:(NSArray<GKPlayer *> *) players;
```

## Discussion

If you do not add at least once recipient, the recipients field is selected when the view controller is presented so that the player can type a list of recipients. Adding more players than defined by the [`maxNumberOfRecipients()`](./maxnumberofrecipients%28%29.md) property causes an exception to be thrown.

## Parameters

- `players`: An array with one or more [`GKPlayer`](../gkplayer.md) objects, each containing an player identifier.

## See Also

### Adding Recipients
- [func addRecipients(withEmailAddresses: [String])](./addrecipients%28withemailaddresses%29.md)
  Adds recipients based on their email addresses.
- [func addRecipients(withPlayerIDs: [String])](./addrecipients%28withplayerids%29.md)
  Adds recipients based on their Game Center player identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/addrecipientplayers(_:))*