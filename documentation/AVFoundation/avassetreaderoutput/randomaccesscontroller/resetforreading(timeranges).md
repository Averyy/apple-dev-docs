# resetForReading(timeRanges:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Starts reading over with a new set of time ranges.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func resetForReading(timeRanges: [CMTimeRange])
```

## Parameters

- `timeRanges`: The time ranges to read

## See Also

### Configuring a controller
- [func markConfigurationAsFinal()](./markconfigurationasfinal%28%29.md)
  Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/resetforreading(timeranges:))*