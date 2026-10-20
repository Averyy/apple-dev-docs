# init(error:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

Creates a publisher that immediately terminates with the specified failure.

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
init(error: Failure)
```

## Parameters

- `error`: The failure to send when terminating the publisher.

## See Also

### Creating a fail publisher
- [init(outputType: Output.Type, failure: Failure)](./init%28outputtype,failure%29.md)
  Creates publisher with the given output type, that immediately terminates with the specified failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/fail/init(error:))*