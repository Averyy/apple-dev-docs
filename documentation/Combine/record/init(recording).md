# init(recording:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

Creates a record publisher from an existing recording.

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
init(recording: Record<Output, Failure>.Recording)
```

## Parameters

- `recording`: A previously-recorded recording of published elements and a completion.

## See Also

### Creating a record publisher
- [init(output: [Output], completion: Subscribers.Completion<Failure>)](./init%28output,completion%29.md)
  Creates a record publisher to publish the provided elements, followed by the provided completion value.
- [init(record: (inout Record<Output, Failure>.Recording) -> Void)](./init%28record%29.md)
  Creates a publisher to interactively record a series of outputs and a completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/init(recording:))*