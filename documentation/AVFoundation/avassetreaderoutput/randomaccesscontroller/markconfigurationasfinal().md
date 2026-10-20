# markConfigurationAsFinal()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Informs the provider that no more reconfiguration of time ranges is necessary and allows the attached AVAssetReader to advance to `AVAssetReaderStatus/completed`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func markConfigurationAsFinal()
```

## See Also

### Configuring a controller
- [func resetForReading(timeRanges: [CMTimeRange])](./resetforreading%28timeranges%29.md)
  Starts reading over with a new set of time ranges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/randomaccesscontroller/markconfigurationasfinal())*