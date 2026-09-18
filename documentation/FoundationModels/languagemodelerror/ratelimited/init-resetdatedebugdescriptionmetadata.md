# init(resetDate:debugDescription:metadata:)

**Framework**: Foundation Models  
**Kind**: init

Creates information describing a rate-limiting event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(resetDate: Date?, debugDescription: String, metadata: [String : any Sendable] = [:])
```

## Parameters

- `resetDate`: The date after which retrying is likely to succeed, or `nil` if unknown.
- `debugDescription`: A debug description to help developers diagnose issues during development.
- `metadata`: Additional information about the failure, keyed by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/ratelimited/init(resetdate:debugdescription:metadata:))*