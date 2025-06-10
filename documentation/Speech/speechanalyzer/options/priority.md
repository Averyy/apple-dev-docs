# priority

**Framework**: Speech  
**Kind**: property

The priority of analysis processing work.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let priority: TaskPriority
```

#### Discussion

This property determines the priority of most, but not all, processing work. You should also call the methods of `SpeechAnalyzer` and other classes from a `Task` or thread with the desired priority.

## See Also

- [let modelRetention: SpeechAnalyzer.Options.ModelRetention](speechanalyzer/options/modelretention-swift.property.md)
  The analyzer’s model caching strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options/priority)*