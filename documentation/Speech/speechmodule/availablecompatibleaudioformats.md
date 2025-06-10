# availableCompatibleAudioFormats

**Framework**: Speech  
**Kind**: property  
**Required**: Yes

The audio formats that this module is able to analyze, given its configuration.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var availableCompatibleAudioFormats: [AVAudioFormat] { get async }
```

#### Discussion

If the audio format doesn’t matter, then there will be one format listed with a sample rate of `kAudioStreamAnyRate` and other values 0.

If assets are necessary yet not installed on device, then the list will be empty.

This property may be accessed before the module is added to the analyzer.

## See Also

- [var results: Self.Results](speechmodule/results-swift.property.md)
  An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule/availablecompatibleaudioformats)*