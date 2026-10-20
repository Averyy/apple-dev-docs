# Executor

**Framework**: Foundation Models  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
associatedtype Executor : LanguageModelExecutor where Self == Self.Executor.Model
```

## See Also

### Getting the executor configuration
- [var executorConfiguration: Self.Executor.Configuration](./executorconfiguration.md)
  A configuration for an executor capable of running this model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodel/executor)*