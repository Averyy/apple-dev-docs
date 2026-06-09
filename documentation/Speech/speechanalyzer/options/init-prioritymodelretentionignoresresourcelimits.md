# init(priority:modelRetention:ignoresResourceLimits:)

**Framework**: Speech  
**Kind**: init

Creates a structure containing analysis processing options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention, ignoresResourceLimits: Bool)
```

#### Discussion

> ⚠️ **Warning**: When setting `ignoresResourceLimits` to `true`, test your app on a variety of devices under a variety of scenarios to experimentally determine how many analyzers you can reliably create and expect to function. Consider how to recover in the event one or more analyzers fail.

## Parameters

- `priority`: A priority to apply to processing work.
- `modelRetention`: A model caching strategy.
- `ignoresResourceLimits`: If `true`, the analyzer and its modules’ resources will not be counted against the predefined system resource limits.

## See Also

- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention)](speechanalyzer/options/init(priority:modelretention:).md)
  Creates a structure containing analysis processing options.
- [SpeechAnalyzer.Options.ModelRetention](speechanalyzer/options/modelretention-swift.enum.md)
  A model caching strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/init(priority:modelretention:ignoresresourcelimits:))*