# init(id:_:)

**Framework**: Foundation Models  
**Kind**: init

Creates a collection that contains the tool calls you provide.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init<S>(id: String = UUID().uuidString, _ calls: S) where S : Sequence, S.Element == Transcript.ToolCall
```

## Parameters

- `id`: A unique identifier for the collection of tool calls.
- `calls`: The tool calls to include, in the order the model generates them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/init(id:_:))*