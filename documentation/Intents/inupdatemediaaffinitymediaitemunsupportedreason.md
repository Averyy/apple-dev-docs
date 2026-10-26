# INUpdateMediaAffinityMediaItemUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons the app can’t update the user’s affinity for the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INUpdateMediaAffinityMediaItemUnsupportedReason
```

```c
enum INUpdateMediaAffinityMediaItemUnsupportedReason : NSInteger;
```

## Topics

### Limitations
- [INUpdateMediaAffinityMediaItemUnsupportedReason.loginRequired](./inupdatemediaaffinitymediaitemunsupportedreason/loginrequired.md)
  The user must log in to the app.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.subscriptionRequired](./inupdatemediaaffinitymediaitemunsupportedreason/subscriptionrequired.md)
  The user must have a subscription to the app’s service.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.unsupportedMediaType](./inupdatemediaaffinitymediaitemunsupportedreason/unsupportedmediatype.md)
  The media’s type is unsupported.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.explicitContentSettings](./inupdatemediaaffinitymediaitemunsupportedreason/explicitcontentsettings.md)
  The explicit content settings don’t allow the user to update the media item’s affinity.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.cellularDataSettings](./inupdatemediaaffinitymediaitemunsupportedreason/cellulardatasettings.md)
  The cellular data settings don’t allow the user to update the media item’s affinity.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.restrictedContent](./inupdatemediaaffinitymediaitemunsupportedreason/restrictedcontent.md)
  The media item is restricted content.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.regionRestriction](./inupdatemediaaffinitymediaitemunsupportedreason/regionrestriction.md)
  The app can’t update the user’s affinity for the media because the media isn’t available in the user’s geographic location.
- [INUpdateMediaAffinityMediaItemUnsupportedReason.serviceUnavailable](./inupdatemediaaffinitymediaitemunsupportedreason/serviceunavailable.md)
  The app can’t update the user’s affinity because the media service is unavailable.
### Initializers
- [init?(rawValue: Int)](./inupdatemediaaffinitymediaitemunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reporting a Problem
- [class func unsupported(forReason: INUpdateMediaAffinityMediaItemUnsupportedReason) -> Self](./inupdatemediaaffinitymediaitemresolutionresult/unsupported%28forreason%29.md)
  Creates a result that requires the user to confirm the request, because your is unable to support the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinitymediaitemunsupportedreason)*