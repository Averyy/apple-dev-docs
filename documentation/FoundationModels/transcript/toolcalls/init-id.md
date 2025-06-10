# init(id:_:)

**Framework**: Foundation Models  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init<C>(id: String = UUID().uuidString, _ calls: C) where C : Collection, C.Element == Transcript.ToolCall
```

## See Also

- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/init(id:_:))*