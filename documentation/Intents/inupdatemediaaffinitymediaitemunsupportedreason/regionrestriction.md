# INUpdateMediaAffinityMediaItemUnsupportedReason.regionRestriction

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app can’t update the user’s affinity for the media because the media isn’t available in the user’s geographic location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case regionRestriction
```

```c
INUpdateMediaAffinityMediaItemUnsupportedReasonRegionRestriction
```

## See Also

### Limitations
- [INUpdateMediaAffinityMediaItemUnsupportedReason.loginRequired](./loginrequired.md)
  The user must log in to the app.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.subscriptionRequired](./subscriptionrequired.md)
  The user must have a subscription to the app’s service.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.unsupportedMediaType](./unsupportedmediatype.md)
  The media’s type is unsupported.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.explicitContentSettings](./explicitcontentsettings.md)
  The explicit content settings don’t allow the user to update the media item’s affinity.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.cellularDataSettings](./cellulardatasettings.md)
  The cellular data settings don’t allow the user to update the media item’s affinity.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.restrictedContent](./restrictedcontent.md)
  The media item is restricted content.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.serviceUnavailable](./serviceunavailable.md)
  The app can’t update the user’s affinity because the media service is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinitymediaitemunsupportedreason/regionrestriction)*