# INAddMediaMediaItemUnsupportedReason.serviceUnavailable

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The media service isn’t available.

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
INAddMediaMediaItemUnsupportedReasonServiceUnavailable
```

## See Also

### Limitations
- [INAddMediaMediaItemUnsupportedReason.loginRequired](./loginrequired.md)
  The user must log in to the app.
- [INAddMediaMediaItemUnsupportedReason.subscriptionRequired](./subscriptionrequired.md)
  The user must have a subscription to the app’s service.
- [INAddMediaMediaItemUnsupportedReason.unsupportedMediaType](./unsupportedmediatype.md)
  The media is an unsupported type.
- [INAddMediaMediaItemUnsupportedReason.explicitContentSettings](./explicitcontentsettings.md)
  The content settings don’t allow the user to add the media item.
- [INAddMediaMediaItemUnsupportedReason.cellularDataSettings](./cellulardatasettings.md)
  The cellular data settings don’t allow the user to add the media item.
- [INAddMediaMediaItemUnsupportedReason.restrictedContent](./restrictedcontent.md)
  The media item is restricted content.
- [INAddMediaMediaItemUnsupportedReason.regionRestriction](./regionrestriction.md)
  The media is unavailable to add in the user’s geographic location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediaitemunsupportedreason/serviceunavailable)*