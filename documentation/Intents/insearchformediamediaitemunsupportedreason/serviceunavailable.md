# INSearchForMediaMediaItemUnsupportedReason.serviceUnavailable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app couldn’t perform the search because the media service is unavailable.

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
INSearchForMediaMediaItemUnsupportedReasonServiceUnavailable
```

## See Also

### Limitations
- [INSearchForMediaMediaItemUnsupportedReason.loginRequired](./loginrequired.md)
  The user must log in to the app in order to search for media.
- [INSearchForMediaMediaItemUnsupportedReason.subscriptionRequired](./subscriptionrequired.md)
  The user must have a subscription to the app’s service in order to search for media.
- [INSearchForMediaMediaItemUnsupportedReason.unsupportedMediaType](./unsupportedmediatype.md)
  The media’s type is not supported.
- [INSearchForMediaMediaItemUnsupportedReason.explicitContentSettings](./explicitcontentsettings.md)
  The content settings don’t allow the user to search for the media item.
- [INSearchForMediaMediaItemUnsupportedReason.cellularDataSettings](./cellulardatasettings.md)
  The cellular data settings don’t allow the user to search for the media item.
- [INSearchForMediaMediaItemUnsupportedReason.restrictedContent](./restrictedcontent.md)
  The media item is restricted content.
- [INSearchForMediaMediaItemUnsupportedReason.regionRestriction](./regionrestriction.md)
  There are media items that match this request, but they aren’t available in the user’s geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediamediaitemunsupportedreason/serviceunavailable)*