# tracks

**Framework**: AVFoundation  
**Kind**: property

The tracks an asset contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var tracks: AVAsyncProperty<Root, [AVAssetTrack]> { get }
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

## See Also

- [func findCompatibleTrack(for: AVCompositionTrack, completionHandler: (AVAssetTrack?, (any Error)?) -> Void)](avurlasset/findcompatibletrack(for:completionhandler:).md)
  Loads an asset track from which you can insert any time range into the composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-44ptx)*