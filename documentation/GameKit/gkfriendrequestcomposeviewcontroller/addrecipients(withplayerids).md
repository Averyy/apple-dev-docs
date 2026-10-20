# addRecipients(withPlayerIDs:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Adds recipients based on their Game Center player identifiers.

**Availability**:
- iOS 4.2+ - Deprecated in 8.0
- iPadOS 4.2+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
func addRecipients(withPlayerIDs playerIDs: [String])
```

```objc
- (void) addRecipientsWithPlayerIDs:(NSArray<NSString *> *) playerIDs;
```

#### Discussion

If you do not add at least once recipient, the recipients field is selected when the view controller is presented so that the player can type a list of recipients.

## Parameters

- `playerIDs`: An array with one or more [`NSString`](../../Foundation/nsstring.md) objects, each containing an player identifier.

## See Also

### Adding Recipients
- [func addRecipients(withEmailAddresses: [String])](./addrecipients%28withemailaddresses%29.md)
  Adds recipients based on their email addresses.
- [func addRecipientPlayers([GKPlayer])](./addrecipientplayers%28_%29.md)
  Adds recipients based on their Game Center player identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/addrecipients(withplayerids:))*