# INPlayMediaMediaItemUnsupportedReason.serviceUnavailable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app can’t add the item because its media service isn’t available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case serviceUnavailable
```

```c
INPlayMediaMediaItemUnsupportedReasonServiceUnavailable
```

## See Also

### Limitations
- [INPlayMediaMediaItemUnsupportedReason.loginRequired](./loginrequired.md)
  The user must log in to the app.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediamediaitemunsupportedreason/serviceunavailable)*