# init(id:_:)

**Framework**: Foundation Models  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init<S>(id: String = UUID().uuidString, _ calls: S) where S : Sequence, S.Element == Transcript.ToolCall
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/init(id:_:))*