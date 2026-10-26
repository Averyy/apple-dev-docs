# INSearchForMediaMediaItemUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons the app can’t provide results for the search.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INSearchForMediaMediaItemUnsupportedReason
```

```c
enum INSearchForMediaMediaItemUnsupportedReason : NSInteger;
```

## Topics

### Limitations
- [INSearchForMediaMediaItemUnsupportedReason.loginRequired](./insearchformediamediaitemunsupportedreason/loginrequired.md)
  The user must log in to the app in order to search for media.
- [INSearchForMediaMediaItemUnsupportedReason.subscriptionRequired](./insearchformediamediaitemunsupportedreason/subscriptionrequired.md)
  The user must have a subscription to the app’s service in order to search for media.
- [INSearchForMediaMediaItemUnsupportedReason.unsupportedMediaType](./insearchformediamediaitemunsupportedreason/unsupportedmediatype.md)
  The media’s type is not supported.
- [INSearchForMediaMediaItemUnsupportedReason.explicitContentSettings](./insearchformediamediaitemunsupportedreason/explicitcontentsettings.md)
  The content settings don’t allow the user to search for the media item.
- [INSearchForMediaMediaItemUnsupportedReason.cellularDataSettings](./insearchformediamediaitemunsupportedreason/cellulardatasettings.md)
  The cellular data settings don’t allow the user to search for the media item.
- [INSearchForMediaMediaItemUnsupportedReason.restrictedContent](./insearchformediamediaitemunsupportedreason/restrictedcontent.md)
  The media item is restricted content.
- [INSearchForMediaMediaItemUnsupportedReason.regionRestriction](./insearchformediamediaitemunsupportedreason/regionrestriction.md)
  There are media items that match this request, but they aren’t available in the user’s geographic location.
- [INSearchForMediaMediaItemUnsupportedReason.serviceUnavailable](./insearchformediamediaitemunsupportedreason/serviceunavailable.md)
  The app couldn’t perform the search because the media service is unavailable.
### Initializers
- [init?(rawValue: Int)](./insearchformediamediaitemunsupportedreason/init%28rawvalue%29.md)

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
- [class func unsupported(forReason: INSearchForMediaMediaItemUnsupportedReason) -> Self](./insearchformediamediaitemresolutionresult/unsupported%28forreason%29.md)
  Creates a result that requires the user to confirm the request because your app is unable to support the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediamediaitemunsupportedreason)*