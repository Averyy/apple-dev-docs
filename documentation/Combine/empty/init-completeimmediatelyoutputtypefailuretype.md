# init(completeImmediately:outputType:failureType:)

**Framework**: Combine  
**Kind**: init

Creates an empty publisher with the given completion behavior and output and failure types.

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
init(completeImmediately: Bool = true, outputType: Output.Type, failureType: Failure.Type)
```

#### Discussion

Use this initializer to connect the empty publisher to subscribers or other publishers that have specific output and failure types.

## Parameters

- `completeImmediately`: A Boolean value that indicates whether the publisher should immediately finish.
- `outputType`: The output type exposed by this publisher.
- `failureType`: The failure type exposed by this publisher.

## See Also

- [init(completeImmediately: Bool)](empty/init(completeimmediately:).md)
  Creates an empty publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/empty/init(completeimmediately:outputtype:failuretype:))*