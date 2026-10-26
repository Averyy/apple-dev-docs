# INAddMediaMediaItemUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons the app can’t add the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INAddMediaMediaItemUnsupportedReason
```

```c
enum INAddMediaMediaItemUnsupportedReason : NSInteger;
```

## Topics

### Limitations
- [INAddMediaMediaItemUnsupportedReason.loginRequired](./inaddmediamediaitemunsupportedreason/loginrequired.md)
  The user must log in to the app.
- [INAddMediaMediaItemUnsupportedReason.subscriptionRequired](./inaddmediamediaitemunsupportedreason/subscriptionrequired.md)
  The user must have a subscription to the app’s service.
- [INAddMediaMediaItemUnsupportedReason.unsupportedMediaType](./inaddmediamediaitemunsupportedreason/unsupportedmediatype.md)
  The media is an unsupported type.
- [INAddMediaMediaItemUnsupportedReason.explicitContentSettings](./inaddmediamediaitemunsupportedreason/explicitcontentsettings.md)
  The content settings don’t allow the user to add the media item.
- [INAddMediaMediaItemUnsupportedReason.cellularDataSettings](./inaddmediamediaitemunsupportedreason/cellulardatasettings.md)
  The cellular data settings don’t allow the user to add the media item.
- [INAddMediaMediaItemUnsupportedReason.restrictedContent](./inaddmediamediaitemunsupportedreason/restrictedcontent.md)
  The media item is restricted content.
- [INAddMediaMediaItemUnsupportedReason.regionRestriction](./inaddmediamediaitemunsupportedreason/regionrestriction.md)
  The media is unavailable to add in the user’s geographic location.
- [INAddMediaMediaItemUnsupportedReason.serviceUnavailable](./inaddmediamediaitemunsupportedreason/serviceunavailable.md)
  The media service isn’t available.
### Initializers
- [init?(rawValue: Int)](./inaddmediamediaitemunsupportedreason/init%28rawvalue%29.md)

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
- [class func unsupported(forReason: INAddMediaMediaItemUnsupportedReason) -> Self](./inaddmediamediaitemresolutionresult/unsupported%28forreason%29.md)
  Creates a result that requires the user to confirm the request because your app is unable to support the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediaitemunsupportedreason)*