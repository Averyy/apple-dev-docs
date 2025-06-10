# results

**Framework**: Speech  
**Kind**: property  
**Required**: Yes

An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var results: Self.Results { get }
```

#### Discussion

Each module has its own result sequence and data structure.

If there is an error in the overall analysis, all modules will throw the error from their individual result sequence.

## See Also

- [var availableCompatibleAudioFormats: [AVAudioFormat]](speechmodule/availablecompatibleaudioformats.md)
  The audio formats that this module is able to analyze, given its configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule/results-swift.property)*