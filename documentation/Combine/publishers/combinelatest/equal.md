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
static func == (lhs: Publishers.CombineLatest<A, B>, rhs: Publishers.CombineLatest<A, B>) -> Bool
```

#### Return Value

`true` if the corresponding upstream publishers of each combineLatest publisher are equal; otherwise `false`.

## Parameters

- `lhs`: A combineLatest publisher to compare for equality.
- `rhs`: Another combineLatest publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/combinelatest/==(_:_:))*