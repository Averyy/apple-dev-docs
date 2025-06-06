# init(outputType:failure:)

**Framework**: Combine  
**Kind**: init

Creates publisher with the given output type, that immediately terminates with the specified failure.

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
init(outputType: Output.Type, failure: Failure)
```

#### Discussion

Use this initializer to create a `Fail` publisher that can work with subscribers or publishers that expect a given output type.

## Parameters

- `outputType`: The output type exposed by this publisher.
- `failure`: The failure to send when terminating the publisher.

## See Also

- [init(error: Failure)](fail/init(error:).md)
  Creates a publisher that immediately terminates with the specified failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/fail/init(outputtype:failure:))*