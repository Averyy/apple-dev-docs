# PlayMediaMediaItemResolutionResult.Unsupported

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

The reason your service can’t play the requested media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object PlayMediaMediaItemResolutionResult.Unsupported
```

#### Discussion

If you can’t find the media item the user specifies, don’t provide a reason. When the client receives an `Unsupported` object without a reason, it provides a generic failure message to the user.

## See Also

- [object PlayMediaMediaItemResolutionResult.Success](playmediamediaitemresolutionresult/success-data.dictionary.md)
  A media item that successfully matches the intent.
- [object PlayMediaMediaItemResolutionResult.Disambiguation](playmediamediaitemresolutionresult/disambiguation-data.dictionary.md)
  A result that requires the user to choose from multiple media items before proceeding.
- [object PlayMediaMediaItemResolutionResult.ConfirmationRequired](playmediamediaitemresolutionresult/confirmationrequired-data.dictionary.md)
  A result that requires the user to confirm the media item before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemresolutionresult/unsupported-data.dictionary)*