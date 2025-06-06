# <(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func < (lhs: Duration, rhs: Duration) -> Bool
```

#### Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/_(_:_:)-ijui)*