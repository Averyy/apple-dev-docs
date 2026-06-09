# priority

**Framework**: Speech  
**Kind**: property

The priority of analysis processing work.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let priority: TaskPriority
```

#### Discussion

This property determines the priority of most, but not all, processing work. You should also call the methods of `SpeechAnalyzer` and other classes from a `Task` or thread with the desired priority.

## See Also

- [let ignoresResourceLimits: Bool](speechanalyzer/options/ignoresresourcelimits.md)
  A Boolean value that indicates whether this analyzer ignores predefined system resource limits.
- [let modelRetention: SpeechAnalyzer.Options.ModelRetention](speechanalyzer/options/modelretention-swift.property.md)
  The analyzer’s model caching strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/priority)*