# init(recording:)

**Framework**: Combine  
**Kind**: init

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

- [init(output: [Output], completion: Subscribers.Completion<Failure>)](record/init(output:completion:).md)
  Creates a record publisher to publish the provided elements, followed by the provided completion value.
- [init(record: (inout Record<Output, Failure>.Recording) -> Void)](record/init(record:).md)
  Creates a publisher to interactively record a series of outputs and a completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/record/init(recording:))*