# ==(_:_:)

**Framework**: Combine  
**Kind**: op  
**Role**: Operator

Returns a Boolean value that indicates whether two publishers are equivalent. /// - Parameters:

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
static func == (lhs: Publishers.Count<Upstream>, rhs: Publishers.Count<Upstream>) -> Bool
```

Available when `Upstream` conforms to `Publisher` and `Equatable`.

## Return Value

`true` if the two publishers’ `upstream` properties are equal; otherwise `false`.

## Discussion

- lhs: A `Count` instance to compare.
- rhs: Another `Count` instance to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/count/==(_:_:))*