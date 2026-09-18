# init(explanation:debugDescription:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates information describing a model refusal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(explanation: String, debugDescription: String, metadata: [String : any Sendable] = [:])
```

## Parameters

- `explanation`: The model’s explanation for why it refused to respond.
- `debugDescription`: A debug description to help developers diagnose issues during development.
- `metadata`: Additional information about the failure, keyed by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/refusal/init(explanation:debugdescription:metadata:))*