# ==(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether two arrays contain the same elements in the same order.

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
static func == (lhs: ContiguousArray<Element>, rhs: ContiguousArray<Element>) -> Bool
```

#### Discussion

You can use the equal-to operator (`==`) to compare any two arrays that store the same, `Equatable`-conforming element type.

## Parameters

- `lhs`: An array to compare.
- `rhs`: Another array to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/==(_:_:))*