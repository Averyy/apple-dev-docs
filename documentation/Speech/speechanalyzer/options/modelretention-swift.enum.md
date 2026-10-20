# SpeechAnalyzer.Options.ModelRetention

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

A model caching strategy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ModelRetention
```

## Topics

### Retention options
- [SpeechAnalyzer.Options.ModelRetention.lingering](./modelretention-swift.enum/lingering.md)
  Keeps the models in memory for a time so that they can be reused by another compatible analyzer session.
- [SpeechAnalyzer.Options.ModelRetention.processLifetime](./modelretention-swift.enum/processlifetime.md)
  Keeps the models in memory until this process exits.
- [SpeechAnalyzer.Options.ModelRetention.whileInUse](./modelretention-swift.enum/whileinuse.md)
  Releases the models when the analyzer is deallocated.

## Relationships

### Conforms To
- [CaseIterable](../../../Swift/caseiterable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating an options object
- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention)](./init%28priority,modelretention%29.md)
  Creates a structure containing analysis processing options.
- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention, ignoresResourceLimits: Bool)](./init%28priority,modelretention,ignoresresourcelimits%29.md)
  Creates a structure containing analysis processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/modelretention-swift.enum)*