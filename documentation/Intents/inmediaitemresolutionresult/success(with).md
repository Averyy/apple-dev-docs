# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a result that contains the media item that matches the user’s request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func success(with resolvedMediaItem: INMediaItem) -> Self
```

```objc
+ (instancetype) successWithResolvedMediaItem:(INMediaItem *) resolvedMediaItem;
```

## Return Value

A new [`INMediaItemResolutionResult`](../inmediaitemresolutionresult.md) object.

## Discussion

Use this method to create a result when your app successfully identifies a single media item to fulfill the intent. For cases where there are potential alternatives, use [`successes(with:)`](./successes%28with%29.md).

## Parameters

- `resolvedMediaItem`: The value that resolves the user’s request. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func successes(with: [INMediaItem]) -> [INMediaItemResolutionResult]](./successes%28with%29.md)
  Creates an array of results that contains the media items that match the user’s request.
- [class func confirmationRequired(with: INMediaItem?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.
- [class func disambiguation(with: [INMediaItem]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitemresolutionresult/success(with:))*