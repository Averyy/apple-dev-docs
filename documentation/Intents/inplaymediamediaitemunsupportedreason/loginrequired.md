# INPlayMediaMediaItemUnsupportedReason.loginRequired

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must log in to the app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case loginRequired
```

```c
INPlayMediaMediaItemUnsupportedReasonLoginRequired
```

## See Also

### Limitations
- [INPlayMediaMediaItemUnsupportedReason.subscriptionRequired](./subscriptionrequired.md)
  The user must have a subscription to the app’s service.
- [INPlayMediaMediaItemUnsupportedReason.unsupportedMediaType](./unsupportedmediatype.md)
  The media’s type is not supported.
- [INPlayMediaMediaItemUnsupportedReason.explicitContentSettings](./explicitcontentsettings.md)
  The content settings don’t allow the user to play the media item.
- [INPlayMediaMediaItemUnsupportedReason.cellularDataSettings](./cellulardatasettings.md)
  The cellular data settings don’t allow the user to play the media item.
- [INPlayMediaMediaItemUnsupportedReason.restrictedContent](./restrictedcontent.md)
  The media item is restricted content.
- [INPlayMediaMediaItemUnsupportedReason.regionRestriction](./regionrestriction.md)
  The media isn’t available in the user’s geographic location.
- [INPlayMediaMediaItemUnsupportedReason.serviceUnavailable](./serviceunavailable.md)
  The app can’t add the item because its media service isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediamediaitemunsupportedreason/loginrequired)*