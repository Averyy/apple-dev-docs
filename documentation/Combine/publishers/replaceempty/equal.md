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
static func == (lhs: Publishers.ReplaceEmpty<Upstream>, rhs: Publishers.ReplaceEmpty<Upstream>) -> Bool
```

#### Return Value

`true` if the two publishers have equal upstream publishers and output elements; otherwise `false`.

## Parameters

- `lhs`: A replace empty publisher to compare for equality.
- `rhs`: Another replace empty publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceempty/==(_:_:))*