# Record.Recording

**Framework**: Combine  
**Kind**: struct

A recorded sequence of outputs, followed by a completion value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Recording
```

## Topics

### Creating a recording
- [init()](record/recording-swift.struct/init.md)
  Set up a recording in a state ready to receive output.
- [init(output: [Output], completion: Subscribers.Completion<Failure>)](record/recording-swift.struct/init(output:completion:).md)
  Set up a complete recording with the specified output and completion.
### Receiving elements
- [func receive(Record<Output, Failure>.Recording.Input)](record/recording-swift.struct/receive(_:).md)
  Add an output to the recording.
### Receiving life cycle events
- [func receive(completion: Subscribers.Completion<Failure>)](record/recording-swift.struct/receive(completion:).md)
  Add a completion to the recording.
### Encoding
- [func encode(into: any Encoder) throws](record/recording-swift.struct/encode(into:).md)
### Inspecting publisher properties
- [var output: [Output]](record/recording-swift.struct/output.md)
  The output which will be sent to a `Subscriber`.
- [var completion: Subscribers.Completion<Failure>](record/recording-swift.struct/completion.md)
  The completion which will be sent to a `Subscriber`.
### Declaring supporting types
- [Record.Recording.Input](record/recording-swift.struct/input.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [let recording: Record<Output, Failure>.Recording](record/recording-swift.property.md)
  The recorded output and completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/recording-swift.struct)*