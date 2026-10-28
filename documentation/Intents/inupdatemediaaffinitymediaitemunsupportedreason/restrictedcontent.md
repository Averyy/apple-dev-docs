# INUpdateMediaAffinityMediaItemUnsupportedReason.restrictedContent

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The media item is restricted content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case restrictedContent
```

```c
INUpdateMediaAffinityMediaItemUnsupportedReasonRestrictedContent
```

## Discussion

Use this reason for geographic region restrictions, or when none of the other, more specific reasons apply.

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
- [INUpdateMediaAffinityMediaItemUnsupportedReason.regionRestriction](./regionrestriction.md)
  The app can’t update the user’s affinity for the media because the media isn’t available in the user’s geographic location.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.serviceUnavailable](./serviceunavailable.md)
  The app can’t update the user’s affinity because the media service is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinitymediaitemunsupportedreason/restrictedcontent)*