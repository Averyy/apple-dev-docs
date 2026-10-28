# findCompatibleTrack(for:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Loads an asset track from which you can insert any time range into the composition track.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func findCompatibleTrack(for compositionTrack: AVCompositionTrack, completionHandler: @escaping @Sendable (AVAssetTrack?, (any Error)?) -> Void)
```

```swift
func findCompatibleTrack(for compositionTrack: AVCompositionTrack) async throws -> AVAssetTrack?
```

```objc
- (void) findCompatibleTrackForCompositionTrack:(AVCompositionTrack *) compositionTrack completionHandler:(void (^)(AVAssetTrack *, NSError *)) completionHandler;
```

## Discussion

This method is the logical complement of [`mutableTrack(compatibleWith:)`](../avmutablecomposition/mutabletrack%28compatiblewith%29.md).

## Parameters

- `compositionTrack`: A composition track to request an asset track for.
- `completionHandler`: A callback the system invokes after it finishes the request. The system calls the completion handler with the following arguments:

  - **track**: The compatible asset track, or `nil` if there isn’t one or an error occurs.
  - **error**: An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVAssetTrack]>](../avpartialasyncproperty/tracks-44ptx.md)
  The tracks an asset contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/findcompatibletrack(for:completionhandler:))*