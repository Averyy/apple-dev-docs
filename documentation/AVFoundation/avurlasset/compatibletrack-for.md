# compatibleTrack(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns an asset track from which you can insert any time range into a given composition track.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func compatibleTrack(for compositionTrack: AVCompositionTrack) -> AVAssetTrack?
```

#### Return Value

An asset track managed by the asset from which any time range can be inserted into a given composition track.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load compatible tracks asynchronously using [`findCompatibleTrack(for:completionHandler:)`](avurlasset/findcompatibletrack(for:completionhandler:).md) instead.

This method is the logical complement of [`mutableTrack(compatibleWith:)`](avmutablecomposition/mutabletrack(compatiblewith:).md).

## Parameters

- `compositionTrack`: The composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avurlasset/compatibletrack(for:))*