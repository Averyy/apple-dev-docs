# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the media destination.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func unsupported(forReason reason: INAddMediaMediaDestinationUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INAddMediaMediaDestinationUnsupportedReason) reason;
```

#### Return Value

A new [`INAddMediaMediaDestinationResolutionResult`](../inaddmediamediadestinationresolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that adding a media item isn’t supported.

## See Also

### Creating a Resolution Result
- [init(mediaDestinationResolutionResult: INMediaDestinationResolutionResult)](./init%28mediadestinationresolutionresult%29.md)
  Creates an object whose resolution involves successfully adding a media item to a particular destination.
- [enum INAddMediaMediaDestinationUnsupportedReason](../inaddmediamediadestinationunsupportedreason.md)
  Reasons describing why the destination is not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediadestinationresolutionresult/unsupported(forreason:))*