# SpeechAnalyzer.Options.ModelRetention.lingering

**Framework**: Speech  
**Kind**: case

Keeps the models in memory for a time so that they can be reused by another compatible analyzer session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case lingering
```

## See Also

- [SpeechAnalyzer.Options.ModelRetention.processLifetime](speechanalyzer/options/modelretention-swift.enum/processlifetime.md)
  Keeps the models in memory until this process exits.
- [SpeechAnalyzer.Options.ModelRetention.whileInUse](speechanalyzer/options/modelretention-swift.enum/whileinuse.md)
  Releases the models when the analyzer is deallocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/modelretention-swift.enum/lingering)*