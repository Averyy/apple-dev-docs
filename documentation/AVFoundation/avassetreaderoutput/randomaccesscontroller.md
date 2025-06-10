# AVAssetReaderOutput.RandomAccessController

**Framework**: AVFoundation  
**Kind**: class

Object used to reset an output provider to read specified time ranges.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class RandomAccessController
```

## Topics

### Instance Methods
- [func markConfigurationAsFinal()](avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal.md)
  Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.
- [func resetForReading(timeRanges: [CMTimeRange])](avassetreaderoutput/randomaccesscontroller/resetforreading(timeranges:).md)
  Starts reading over with a new set of time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller)*