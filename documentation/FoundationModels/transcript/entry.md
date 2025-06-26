# Transcript.Entry

**Framework**: Foundation Models  
**Kind**: enum

An entry in a transcript.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Entry
```

## Topics

### Creating an entry
- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [case instructions(Transcript.Instructions)](transcript/entry/instructions(_:).md)
  Instructions, typically provided by you, the developer.
- [case prompt(Transcript.Prompt)](transcript/entry/prompt(_:).md)
  A prompt, typically sourced from an end user.
- [case response(Transcript.Response)](transcript/entry/response(_:).md)
  A response from the model.
- [case toolCalls(Transcript.ToolCalls)](transcript/entry/toolcalls(_:).md)
  A tool call containing a tool name and the arguments to invoke it with.
- [case toolOutput(Transcript.ToolOutput)](transcript/entry/tooloutput(_:).md)
  An tool output provided back to the model.
### Inspecting an entry
- [var id: String](transcript/entry/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [Transcript.Entry.ID](transcript/entry/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Encoding an entry
- [func encode(to: any Encoder) throws](transcript/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing entries
- [static func == (Transcript.Entry, Transcript.Entry) -> Bool](transcript/entry/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomStringConvertible Implementations](transcript/entry/customstringconvertible-implementations.md)
- [Equatable Implementations](transcript/entry/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(entries: some Sequence<Transcript.Entry>)](transcript/init(entries:).md)
  Creates a transcript.
- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [Transcript.Segment](transcript/segment.md)
  The types of segments that may be included in a transcript entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/entry)*