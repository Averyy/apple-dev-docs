# PlayMediaMediaItemResolutionResult.ConfirmationRequired

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

A result that requires the user to confirm the media item before proceeding.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaMediaItemResolutionResult.ConfirmationRequired
```

#### Discussion

Prefer to provide a successful result, even if you aren’t sure that you’re identifying the media item accurately. The user can cancel playback and try asking again.

## See Also

- [object PlayMediaMediaItemResolutionResult.Success](playmediamediaitemresolutionresult/success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object PlayMediaMediaItemResolutionResult.Unsupported](playmediamediaitemresolutionresult/unsupported-data.dictionary.md)
  The reason your service can’t play the requested media item.
- [object PlayMediaMediaItemResolutionResult.Disambiguation](playmediamediaitemresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemresolutionresult/confirmationrequired-data.dictionary)*