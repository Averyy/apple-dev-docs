# resolveMediaItems(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the media items to play.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveMediaItems(for intent: INPlayMediaIntent, with completion: @escaping @Sendable ([INPlayMediaMediaItemResolutionResult]) -> Void)
```

```swift
optional func resolveMediaItems(for intent: INPlayMediaIntent) async -> [INPlayMediaMediaItemResolutionResult]
```

```objc
- (void) resolveMediaItemsForPlayMedia:(INPlayMediaIntent *) intent withCompletion:(void (^)(NSArray<INPlayMediaMediaItemResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

> ❗ **Important**:  You must implement this resolve method. The other resolve methods in this protocol are optional.

Implement this method to resolve the media items to play. If your app isn’t completely sure of the match, return a few results with the best match first. The system can start playing the first item and offer the alternatives in case the user wants to play one of them instead.

## Parameters

- `intent`: The object that contains details about the user’s request. Use this object to get any initial information the user may have provided.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution.

## See Also

### Resolving the Intent Parameters
- [func resolvePlayShuffled(for: INPlayMediaIntent, with: (INBooleanResolutionResult) -> Void)](./resolveplayshuffled%28for,with%29.md)
  Resolves whether to shuffle the played media.
- [func resolvePlaybackQueueLocation(for: INPlayMediaIntent, with: (INPlaybackQueueLocationResolutionResult) -> Void)](./resolveplaybackqueuelocation%28for,with%29.md)
  Resolves the location in the playback queue where your app plays the media.
- [func resolvePlaybackRepeatMode(for: INPlayMediaIntent, with: (INPlaybackRepeatModeResolutionResult) -> Void)](./resolveplaybackrepeatmode%28for,with%29.md)
  Resolves the repeat mode when playing media.
- [func resolvePlaybackSpeed(for: INPlayMediaIntent, with: (INPlayMediaPlaybackSpeedResolutionResult) -> Void)](./resolveplaybackspeed%28for,with%29.md)
  Resolves the playback speed when playing media.
- [func resolveResumePlayback(for: INPlayMediaIntent, with: (INBooleanResolutionResult) -> Void)](./resolveresumeplayback%28for,with%29.md)
  Resolves whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintenthandling/resolvemediaitems(for:with:))*