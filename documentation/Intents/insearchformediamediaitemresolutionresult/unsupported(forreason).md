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
class func unsupported(forReason reason: INSearchForMediaMediaItemUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INSearchForMediaMediaItemUnsupportedReason) reason;
```

## Return Value

A new [`INSearchForMediaMediaItemResolutionResult`](../insearchformediamediaitemresolutionresult.md) object.

## Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that playing the media item isn’t supported.

## See Also

### Reporting a Problem
- [enum INSearchForMediaMediaItemUnsupportedReason](../insearchformediamediaitemunsupportedreason.md)
  Reasons the app can’t provide results for the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediamediaitemresolutionresult/unsupported(forreason:))*