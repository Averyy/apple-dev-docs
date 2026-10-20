# timedMetadataGroup

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A timed metadata group containing the Cinematic video metadata.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var timedMetadataGroup: AVTimedMetadataGroup? { get }
```

```objc
@property (nonatomic, readonly, nullable) AVTimedMetadataGroup * timedMetadataGroup;
```

#### Discussion

Append this group to an [`AVAssetWriterInputMetadataAdaptor`](../avassetwriterinputmetadataadaptor.md) to write the Cinematic video metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatacinematicvideometadataobject/timedmetadatagroup)*