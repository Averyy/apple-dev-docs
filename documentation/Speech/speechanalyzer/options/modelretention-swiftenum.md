# SpeechAnalyzer.Options.ModelRetention

**Framework**: Speech  
**Kind**: enum

A model caching strategy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ModelRetention
```

## Topics

### Retention options
- [SpeechAnalyzer.Options.ModelRetention.lingering](speechanalyzer/options/modelretention-swift.enum/lingering.md)
  Keeps the models in memory for a time so that they can be reused by another compatible analyzer session.
- [SpeechAnalyzer.Options.ModelRetention.processLifetime](speechanalyzer/options/modelretention-swift.enum/processlifetime.md)
  Keeps the models in memory until this process exits.
- [SpeechAnalyzer.Options.ModelRetention.whileInUse](speechanalyzer/options/modelretention-swift.enum/whileinuse.md)
  Releases the models when the analyzer is deallocated.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention)](speechanalyzer/options/init(priority:modelretention:).md)
  Creates a structure containing analysis processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/modelretention-swift.enum)*