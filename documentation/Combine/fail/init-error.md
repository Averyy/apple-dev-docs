# init(error:)

**Framework**: Combine  
**Kind**: init

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

- [init(outputType: Output.Type, failure: Failure)](fail/init(outputtype:failure:).md)
  Creates publisher with the given output type, that immediately terminates with the specified failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/fail/init(error:))*