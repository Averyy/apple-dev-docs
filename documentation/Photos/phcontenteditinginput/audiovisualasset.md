# audiovisualAsset

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The video asset, as an `AVAsset` object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var audiovisualAsset: AVAsset? { get }
```

```objc
@property (strong, readonly, nullable) AVAsset * audiovisualAsset;
```

#### Discussion

This object provides access to the video asset as a collection of tracks and metadata. For details on working with [`AVAsset`](../../AVFoundation/avasset.md) objects, see [AVFoundation Programming Guide](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188).

## See Also

### Working with Video Assets
- [var avAsset: AVAsset?](./avasset.md)
  The video asset, as an `AVAsset` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/audiovisualasset)*