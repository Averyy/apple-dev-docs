# init(record:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

Creates a publisher to interactively record a series of outputs and a completion.

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
init(record: (inout Record<Output, Failure>.Recording) -> Void)
```

## Parameters

- `record`: A recording instance that can be retrieved after completion to create new record publishers to replay the recording.

## See Also

### Creating a record publisher
- [init(output: [Output], completion: Subscribers.Completion<Failure>)](./init%28output,completion%29.md)
  Creates a record publisher to publish the provided elements, followed by the provided completion value.
- [init(recording: Record<Output, Failure>.Recording)](./init%28recording%29.md)
  Creates a record publisher from an existing recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/init(record:))*