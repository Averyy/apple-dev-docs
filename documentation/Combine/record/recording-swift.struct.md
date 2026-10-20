# Record.Recording

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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
- [init()](./recording-swift.struct/init%28%29.md)
  Set up a recording in a state ready to receive output.
- [init(output: [Output], completion: Subscribers.Completion<Failure>)](./recording-swift.struct/init%28output,completion%29.md)
  Set up a complete recording with the specified output and completion.
### Receiving elements
- [func receive(Record<Output, Failure>.Recording.Input)](./recording-swift.struct/receive%28_%29.md)
  Add an output to the recording.
### Receiving life cycle events
- [func receive(completion: Subscribers.Completion<Failure>)](./recording-swift.struct/receive%28completion%29.md)
  Add a completion to the recording.
### Encoding
- [func encode(into: any Encoder) throws](./recording-swift.struct/encode%28into%29.md)
### Inspecting publisher properties
- [var output: [Output]](./recording-swift.struct/output.md)
  The output which will be sent to a `Subscriber`.
- [var completion: Subscribers.Completion<Failure>](./recording-swift.struct/completion.md)
  The completion which will be sent to a `Subscriber`.
### Declaring supporting types
- [Record.Recording.Input](./recording-swift.struct/input.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Inspecting publisher properties
- [let recording: Record<Output, Failure>.Recording](./recording-swift.property.md)
  The recorded output and completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/recording-swift.struct)*