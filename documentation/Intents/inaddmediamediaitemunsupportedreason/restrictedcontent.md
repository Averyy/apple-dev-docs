# INAddMediaMediaItemUnsupportedReason.restrictedContent

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
INAddMediaMediaItemUnsupportedReasonRestrictedContent
```

## Discussion

Use this reason for geographic region restrictions, or when none of the other, more specific reasons apply.

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
- [INAddMediaMediaItemUnsupportedReason.regionRestriction](./regionrestriction.md)
  The media is unavailable to add in the user’s geographic location.
- [INAddMediaMediaItemUnsupportedReason.serviceUnavailable](./serviceunavailable.md)
  The media service isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediaitemunsupportedreason/restrictedcontent)*