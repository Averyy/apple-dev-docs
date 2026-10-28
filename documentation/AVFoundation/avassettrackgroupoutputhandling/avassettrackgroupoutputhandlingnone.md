# AVAssetTrackGroupOutputHandlingNone

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Enumeration Case

A policy that doesn’t pass through alternate audio tracks from the source asset during export.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```c
AVAssetTrackGroupOutputHandlingNone
```

## Discussion

Setting this policy tells the session to disregard alternate track group assignments in the original asset.

## See Also

### Policies
- [static var preserveAlternateTracks: AVAssetTrackGroupOutputHandling](./preservealternatetracks.md)
  A policy that passes through alternate audio tracks from the source asset during export.
- [AVAssetTrackGroupOutputHandlingDefaultPolicy](./avassettrackgroupoutputhandlingdefaultpolicy.md)
  The default track group output handling policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrackgroupoutputhandling/avassettrackgroupoutputhandlingnone)*