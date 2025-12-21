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
static func == (lhs: Publishers.CollectByCount<Upstream>, rhs: Publishers.CollectByCount<Upstream>) -> Bool
```

#### Return Value

`true` if the corresponding `upstream` and `count` properties of each publisher are equal; otherwise `false`.

## Parameters

- `lhs`: A   instance to compare.
- `rhs`: Another   instance to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collectbycount/==(_:_:))*