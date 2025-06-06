# error

**Framework**: Foundation  
**Kind**: property

The error object representing the last authentication failure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

This value is `nil` if the protocol doesn’t use errors to indicate an authentication failure.

## See Also

- [var failureResponse: URLResponse?](urlauthenticationchallenge/failureresponse.md)
  The URL response object representing the last authentication failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/error)*