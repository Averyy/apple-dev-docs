# markConfigurationAsFinal()

**Framework**: AVFoundation  
**Kind**: method

Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func markConfigurationAsFinal()
```

## See Also

- [func resetForReading(timeRanges: [CMTimeRange])](avassetreaderoutput/randomaccesscontroller/resetforreading(timeranges:).md)
  Starts reading over with a new set of time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal())*