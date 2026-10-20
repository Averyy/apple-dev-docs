# contextSize

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

The model’s maximum context size, in tokens.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var contextSize: Int
```

## See Also

### Inspecting context size errors
- [var metadata: [String : any Sendable]](./metadata.md)
  Additional information about the failure, keyed by name.
- [var tokenCount: Int](./tokencount.md)
  The number of tokens in the transcript that exceeded the model’s context size.
- [var debugDescription: String](./debugdescription.md)
  A debug description to help developers diagnose issues during development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/contextsizeexceeded/contextsize)*