# successes(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an array of results that contains the media items that match the user’s request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func successes(with resolvedMediaItems: [INMediaItem]) -> [INMediaItemResolutionResult]
```

```objc
+ (NSArray<__kindof INMediaItemResolutionResult *> *) successesWithResolvedMediaItems:(NSArray<INMediaItem *> *) resolvedMediaItems;
```

#### Return Value

The array of [`INMediaItemResolutionResult`](../inmediaitemresolutionresult.md) objects.

#### Discussion

Use this method to create results when your app successfully identifies multiple media items to fulfill the same intent. After the first item in the list, any media item suggestions display as alternatives, but only on iOS. For cases where there are no potential alternatives, use [`success(with:)`](./success%28with%29.md).

## Parameters

- `resolvedMediaItems`: An array of [`INMediaItem`](../inmediaitem.md) objects that resolve the user’s request. These values may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INMediaItem) -> Self](./success%28with%29.md)
  Creates a result that contains the media item that matches the user’s request.
- [class func confirmationRequired(with: INMediaItem?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.
- [class func disambiguation(with: [INMediaItem]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitemresolutionresult/successes(with:))*