# availableCompatibleAudioFormats

**Framework**: Speech  
**Kind**: property  
**Required**: Yes

The audio formats that this module is able to analyze, given its configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var availableCompatibleAudioFormats: [AVAudioFormat] { get async }
```

#### Discussion

If the audio format doesn’t matter, then there will be one format listed with a sample rate of `kAudioStreamAnyRate` and other values 0.

If assets are necessary yet not installed on device, then the list will be empty.

This property may be accessed before the module is added to the analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule/availablecompatibleaudioformats)*