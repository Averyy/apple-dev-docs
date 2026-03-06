# <(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static func < (lhs: EnumeratedSequence<Base>.Index, rhs: EnumeratedSequence<Base>.Index) -> Bool
```

#### Discussion

This function is the only requirement of the `Comparable` protocol. The remainder of the relational operator functions are implemented by the standard library for any type that conforms to `Comparable`.

## Parameters

- `lhs`: A value to compare.
- `rhs`: Another value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/index/_(_:_:))*