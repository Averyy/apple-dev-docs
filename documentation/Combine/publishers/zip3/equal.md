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
static func == (lhs: Publishers.Zip3<A, B, C>, rhs: Publishers.Zip3<A, B, C>) -> Bool
```

#### Return Value

`true` if the corresponding upstream publishers of each zip publisher are equal; otherwise `false`.

## Parameters

- `lhs`: A zip publisher to compare for equality.
- `rhs`: Another zip publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip3/==(_:_:))*