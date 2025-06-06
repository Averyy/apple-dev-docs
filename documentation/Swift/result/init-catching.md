# init(catching:)

**Framework**: Swift  
**Kind**: init

Creates a new result by evaluating a throwing closure, capturing the returned value as a success, or any thrown error as a failure.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(catching body: () throws(Failure) -> Success)
```

## Mentions

- [Preserving the Results of a Throwing Expression](preserving-the-results-of-a-throwing-expression.md)

## Parameters

- `body`: A potentially throwing closure to evaluate.

## See Also

- [Preserving the Results of a Throwing Expression](preserving-the-results-of-a-throwing-expression.md)
  Call the initializer that wraps a throwing expression when you need to serialize or memoize the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/result/init(catching:))*