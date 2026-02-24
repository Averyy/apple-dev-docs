# ==(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value that indicates whether two publishers are equivalent.

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
static func == (lhs: Publishers.Concatenate<Prefix, Suffix>, rhs: Publishers.Concatenate<Prefix, Suffix>) -> Bool
```

#### Return Value

`true` if the two publishers’ `prefix` and `suffix` properties are equal; otherwise `false`.

## Parameters

- `lhs`: A concatenate publisher to compare for equality.
- `rhs`: Another concatenate publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/concatenate/==(_:_:))*