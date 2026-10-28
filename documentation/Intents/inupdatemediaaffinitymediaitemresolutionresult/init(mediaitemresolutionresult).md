# init(mediaItemResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a result that involves successfully updating the user’s affinity for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mediaItemResolutionResult: INMediaItemResolutionResult)
```

```objc
- (instancetype) initWithMediaItemResolutionResult:(INMediaItemResolutionResult *) mediaItemResolutionResult;
```

## Return Value

A new [`INUpdateMediaAffinityMediaItemResolutionResult`](../inupdatemediaaffinitymediaitemresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to successfully update the user’s affinity for a media item.

## Parameters

- `mediaItemResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Providing Successful Results
- [class func successes(with: [INMediaItem]) -> [INUpdateMediaAffinityMediaItemResolutionResult]](./successes%28with%29.md)
  Creates an array of resolution results based on a set of media items you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinitymediaitemresolutionresult/init(mediaitemresolutionresult:))*