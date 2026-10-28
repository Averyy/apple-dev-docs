# compatibleTrack(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an asset track from which you can insert any time range into a given composition track.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`findCompatibleTrack(for:completionHandler:)`](./findcompatibletrack%28for,completionhandler%29.md) instead.

## Declaration

```swift
func compatibleTrack(for compositionTrack: AVCompositionTrack) -> AVAssetTrack?
```

```objc
- (AVAssetTrack *) compatibleTrackForCompositionTrack:(AVCompositionTrack *) compositionTrack;
```

## Return Value

An asset track managed by the asset from which any time range can be inserted into a given composition track.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load compatible tracks asynchronously using [`findCompatibleTrack(for:completionHandler:)`](./findcompatibletrack%28for,completionhandler%29.md) instead.

This method is the logical complement of [`mutableTrack(compatibleWith:)`](../avmutablecomposition/mutabletrack%28compatiblewith%29.md).

## Parameters

- `compositionTrack`: The composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/compatibletrack(for:))*