# init(output:completion:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

Creates a record publisher to publish the provided elements, followed by the provided completion value.

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
init(output: [Output], completion: Subscribers.Completion<Failure>)
```

## Parameters

- `output`: An array of output elements to publish.
- `completion`: The completion value with which to end publishing.

## See Also

### Creating a record publisher
- [init(record: (inout Record<Output, Failure>.Recording) -> Void)](./init%28record%29.md)
  Creates a publisher to interactively record a series of outputs and a completion.
- [init(recording: Record<Output, Failure>.Recording)](./init%28recording%29.md)
  Creates a record publisher from an existing recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/init(output:completion:))*