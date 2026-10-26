# INPlayMediaMediaItemUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons the app can’t play the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INPlayMediaMediaItemUnsupportedReason
```

```c
enum INPlayMediaMediaItemUnsupportedReason : NSInteger;
```

## Topics

### Limitations
- [INPlayMediaMediaItemUnsupportedReason.loginRequired](./inplaymediamediaitemunsupportedreason/loginrequired.md)
  The user must log in to the app.
- [INPlayMediaMediaItemUnsupportedReason.subscriptionRequired](./inplaymediamediaitemunsupportedreason/subscriptionrequired.md)
  The user must have a subscription to the app’s service.
- [INPlayMediaMediaItemUnsupportedReason.unsupportedMediaType](./inplaymediamediaitemunsupportedreason/unsupportedmediatype.md)
  The media’s type is not supported.
- [INPlayMediaMediaItemUnsupportedReason.explicitContentSettings](./inplaymediamediaitemunsupportedreason/explicitcontentsettings.md)
  The content settings don’t allow the user to play the media item.
- [INPlayMediaMediaItemUnsupportedReason.cellularDataSettings](./inplaymediamediaitemunsupportedreason/cellulardatasettings.md)
  The cellular data settings don’t allow the user to play the media item.
- [INPlayMediaMediaItemUnsupportedReason.restrictedContent](./inplaymediamediaitemunsupportedreason/restrictedcontent.md)
  The media item is restricted content.
- [INPlayMediaMediaItemUnsupportedReason.regionRestriction](./inplaymediamediaitemunsupportedreason/regionrestriction.md)
  The media isn’t available in the user’s geographic location.
- [INPlayMediaMediaItemUnsupportedReason.serviceUnavailable](./inplaymediamediaitemunsupportedreason/serviceunavailable.md)
  The app can’t add the item because its media service isn’t available.
### Initializers
- [init?(rawValue: Int)](./inplaymediamediaitemunsupportedreason/init%28rawvalue%29.md)

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
- [class func unsupported(forReason: INPlayMediaMediaItemUnsupportedReason) -> Self](./inplaymediamediaitemresolutionresult/unsupported%28forreason%29.md)
  Creates a result that requires the user to confirm the request, because your app is unable to support the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediamediaitemunsupportedreason)*