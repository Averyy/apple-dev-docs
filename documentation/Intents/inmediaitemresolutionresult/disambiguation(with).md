# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class func disambiguation(with mediaItemsToDisambiguate: [INMediaItem]) -> Self
```

```objc
+ (instancetype) disambiguationWithMediaItemsToDisambiguate:(NSArray<INMediaItem *> *) mediaItemsToDisambiguate;
```

## Return Value

A new [`INMediaItemResolutionResult`](../inmediaitemresolutionresult.md) object.

## Discussion

Use this method to create a result object when more than one media item matches the given information and you can’t definitively pick one. Ask the user to select from among the notes that you specify.

For each [`INMediaItem`](../inmediaitem.md) object that you provide, include enough information to be able to locate the media item later. When the user selects one of the destinations, SiriKit puts the details from your [`INMediaItem`](../inmediaitem.md) object into the intent and asks you to resolve the media item again.

## Parameters

- `mediaItemsToDisambiguate`: An array of [`INMediaItem`](../inmediaitem.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INMediaItem) -> Self](./success%28with%29.md)
  Creates a result that contains the media item that matches the user’s request.
- [class func successes(with: [INMediaItem]) -> [INMediaItemResolutionResult]](./successes%28with%29.md)
  Creates an array of results that contains the media items that match the user’s request.
- [class func confirmationRequired(with: INMediaItem?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitemresolutionresult/disambiguation(with:))*