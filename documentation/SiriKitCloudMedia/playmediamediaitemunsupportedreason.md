# PlayMediaMediaItemUnsupportedReason

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Reasons the media service can’t play the media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string PlayMediaMediaItemUnsupportedReason
```

## Possible Values

- `loginRequired`: The user must log in to the service.
- `subscriptionRequired`: The user must have an active subscription to play the media item.
- `unsupportedMediaType`: Your service doesn’t support the media item’s type.
- `explicitContentSettings`: The content settings don’t allow the user to play the media item.
- `restrictedContent`: The media item is restricted content.
- `regionRestriction`: The media item isn’t available in the user’s geographic location.

## See Also

### Resolving a Media Item
- [object PlayMediaIntentHandlingResolveMediaItemsInvocationResponse](./playmediaintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in a play media intent.
- [object PlayMediaMediaItemResolutionResult](./playmediamediaitemresolutionresult.md)
  A media item that matches a play media intent, or information about why your service can’t provide a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/playmediamediaitemunsupportedreason)*