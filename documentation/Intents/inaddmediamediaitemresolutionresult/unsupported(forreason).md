# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that requires the user to confirm the request because your app is unable to support the current request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func unsupported(forReason reason: INAddMediaMediaItemUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INAddMediaMediaItemUnsupportedReason) reason;
```

#### Return Value

A new [`INAddMediaMediaItemResolutionResult`](../inaddmediamediaitemresolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that adding a media item isn’t supported.

## See Also

### Reporting a Problem
- [enum INAddMediaMediaItemUnsupportedReason](../inaddmediamediaitemunsupportedreason.md)
  Reasons the app can’t add the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediaitemresolutionresult/unsupported(forreason:))*