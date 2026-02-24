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
static func == (lhs: Publishers.Merge7<A, B, C, D, E, F, G>, rhs: Publishers.Merge7<A, B, C, D, E, F, G>) -> Bool
```

#### Return Value

`true` if the two merging publishers have equal source publishers; otherwise `false`.

## Parameters

- `lhs`: A merging publisher to compare for equality.
- `rhs`: Another merging publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge7/==(_:_:))*