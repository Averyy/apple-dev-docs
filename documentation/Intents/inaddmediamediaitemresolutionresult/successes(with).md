# successes(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an array of resolution results based on a set of media items you provide.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func successes(with resolvedMediaItems: [INMediaItem]) -> [INAddMediaMediaItemResolutionResult]
```

```objc
+ (NSArray<INAddMediaMediaItemResolutionResult *> *) successesWithResolvedMediaItems:(NSArray<INMediaItem *> *) resolvedMediaItems;
```

## Return Value

An array of new [`INAddMediaMediaItemResolutionResult`](../inaddmediamediaitemresolutionresult.md) objects.

## Discussion

When the system calls [`resolveMediaItems(for:with:)`](../inaddmediaintenthandling/resolvemediaitems%28for,with%29.md), if your app can identify relevant media for the intent, use this method to create results for each of those media items.

## Parameters

- `resolvedMediaItems`: The items that are relevant for the user’s intent.

## See Also

### Providing Successful Results
- [init(mediaItemResolutionResult: INMediaItemResolutionResult)](./init%28mediaitemresolutionresult%29.md)
  Creates a result that involves successfully adding a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediaitemresolutionresult/successes(with:))*