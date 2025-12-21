# SpeechAnalyzer.Options.ModelRetention.whileInUse

**Framework**: Speech  
**Kind**: case

Releases the models when the analyzer is deallocated.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case whileInUse
```

## See Also

- [SpeechAnalyzer.Options.ModelRetention.lingering](speechanalyzer/options/modelretention-swift.enum/lingering.md)
  Keeps the models in memory for a time so that they can be reused by another compatible analyzer session.
- [SpeechAnalyzer.Options.ModelRetention.processLifetime](speechanalyzer/options/modelretention-swift.enum/processlifetime.md)
  Keeps the models in memory until this process exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/modelretention-swift.enum/whileinuse)*