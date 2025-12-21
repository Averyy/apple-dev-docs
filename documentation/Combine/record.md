# Record

**Framework**: Combine  
**Kind**: struct

A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.

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
struct Record<Output, Failure> where Failure : Error
```

## Topics

### Creating a record publisher
- [init(output: [Output], completion: Subscribers.Completion<Failure>)](record/init(output:completion:).md)
  Creates a record publisher to publish the provided elements, followed by the provided completion value.
- [init(record: (inout Record<Output, Failure>.Recording) -> Void)](record/init(record:).md)
  Creates a publisher to interactively record a series of outputs and a completion.
- [init(recording: Record<Output, Failure>.Recording)](record/init(recording:).md)
  Creates a record publisher from an existing recording.
### Inspecting publisher properties
- [let recording: Record<Output, Failure>.Recording](record/recording-swift.property.md)
  The recorded output and completion.
- [Record.Recording](record/recording-swift.struct.md)
  A recorded sequence of outputs, followed by a completion value.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Publisher](publisher.md)

## See Also

- [class Future](future.md)
  A publisher that eventually produces a single value and then finishes or fails.
- [struct Just](just.md)
  A publisher that emits an output to each subscriber just once, and then finishes.
- [struct Deferred](deferred.md)
  A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [struct Empty](empty.md)
  A publisher that never publishes any values, and optionally finishes immediately.
- [struct Fail](fail.md)
  A publisher that immediately terminates with the specified error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record)*