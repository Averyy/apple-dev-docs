# init(schemaName:debugDescription:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates information describing a generation guide the model doesn’t support.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(schemaName: String?, debugDescription: String, metadata: [String : any Sendable] = [:])
```

## Parameters

- `schemaName`: The name of the schema whose generation guide isn’t supported, if any.
- `debugDescription`: A debug description to help developers diagnose issues during development.
- `metadata`: Additional information about the failure, keyed by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedgenerationguide/init(schemaname:debugdescription:metadata:))*