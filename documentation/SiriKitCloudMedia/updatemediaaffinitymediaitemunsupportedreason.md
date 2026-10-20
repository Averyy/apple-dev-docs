# UpdateMediaAffinityMediaItemUnsupportedReason

**Framework**: SiriKit Cloud Media  
**Kind**: typealias  
**Role**: Type

Reasons the media service can’t update information about the media item.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```
string UpdateMediaAffinityMediaItemUnsupportedReason
```

## Possible Values

- `loginRequired`: The user must log in to the service.
- `subscriptionRequired`: The user must have an active subscription.
- `unsupportedMediaType`: Your service doesn’t support tthe media item’s type.
- `explicitContentSettings`: The content settings don’t allow the user to access the media item.
- `regionRestriction`
- `restrictedContent`
- `serviceUnavailable`

## See Also

### Identifying the Intended Media Items
- [object UpdateMediaAffinityIntentHandlingResolveMediaItemsInvocationResponse](./updatemediaaffinityintenthandlingresolvemediaitemsinvocationresponse.md)
  Your service’s response to a request to resolve media items in an update media affinity intent.
- [object UpdateMediaAffinityMediaItemResolutionResult](./updatemediaaffinitymediaitemresolutionresult.md)
  A media item that matches an update media affinity intent, or information about why your service can’t provide a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinitymediaitemunsupportedreason)*