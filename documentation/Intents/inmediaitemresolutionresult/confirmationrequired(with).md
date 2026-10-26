# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the value before proceeding.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func confirmationRequired(with mediaItemToConfirm: INMediaItem?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithMediaItemToConfirm:(INMediaItem *) mediaItemToConfirm;
```

#### Return Value

A new [`INMediaItemResolutionResult`](../inmediaitemresolutionresult.md) object.

#### Discussion

Use this method when you can’t resolve the parameter to a media item that’s similar, but not equal to, the one specified in the intent. Don’t use this method to resolve media items your app doesn’t support.

## Parameters

- `mediaItemToConfirm`: The value that resolves the request, but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INMediaItem) -> Self](./success%28with%29.md)
  Creates a result that contains the media item that matches the user’s request.
- [class func successes(with: [INMediaItem]) -> [INMediaItemResolutionResult]](./successes%28with%29.md)
  Creates an array of results that contains the media items that match the user’s request.
- [class func disambiguation(with: [INMediaItem]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitemresolutionresult/confirmationrequired(with:))*