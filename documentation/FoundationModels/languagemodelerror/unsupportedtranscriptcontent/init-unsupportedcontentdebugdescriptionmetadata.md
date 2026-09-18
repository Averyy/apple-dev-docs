# init(unsupportedContent:debugDescription:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates information describing transcript content the model can’t process.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(unsupportedContent: [Transcript.Entry], debugDescription: String, metadata: [String : any Sendable] = [:])
```

## Parameters

- `unsupportedContent`: The transcript entries that the model can’t process.
- `debugDescription`: A debug description to help developers diagnose issues during development.
- `metadata`: Additional information about the failure, keyed by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedtranscriptcontent/init(unsupportedcontent:debugdescription:metadata:))*