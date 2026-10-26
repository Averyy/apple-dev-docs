# resolvePlaybackRepeatMode(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the repeat mode when playing media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolvePlaybackRepeatMode(for intent: INPlayMediaIntent, with completion: @escaping @Sendable (INPlaybackRepeatModeResolutionResult) -> Void)
```

```swift
optional func resolvePlaybackRepeatMode(for intent: INPlayMediaIntent) async -> INPlaybackRepeatModeResolutionResult
```

```objc
- (void) resolvePlaybackRepeatModeForPlayMedia:(INPlayMediaIntent *) intent withCompletion:(void (^)(INPlaybackRepeatModeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve which repeat mode to use when playing media.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution object that contains the [`INPlaybackRepeatMode`](../inplaybackrepeatmode.md) value.

## See Also

### Resolving the Intent Parameters
- [func resolveMediaItems(for: INPlayMediaIntent, with: ([INPlayMediaMediaItemResolutionResult]) -> Void)](./resolvemediaitems%28for,with%29.md)
  Resolves the media items to play.
- [func resolvePlayShuffled(for: INPlayMediaIntent, with: (INBooleanResolutionResult) -> Void)](./resolveplayshuffled%28for,with%29.md)
  Resolves whether to shuffle the played media.
- [func resolvePlaybackQueueLocation(for: INPlayMediaIntent, with: (INPlaybackQueueLocationResolutionResult) -> Void)](./resolveplaybackqueuelocation%28for,with%29.md)
  Resolves the location in the playback queue where your app plays the media.
- [func resolvePlaybackSpeed(for: INPlayMediaIntent, with: (INPlayMediaPlaybackSpeedResolutionResult) -> Void)](./resolveplaybackspeed%28for,with%29.md)
  Resolves the playback speed when playing media.
- [func resolveResumePlayback(for: INPlayMediaIntent, with: (INBooleanResolutionResult) -> Void)](./resolveresumeplayback%28for,with%29.md)
  Resolves whether to resume playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintenthandling/resolveplaybackrepeatmode(for:with:))*