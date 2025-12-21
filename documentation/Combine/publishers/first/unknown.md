# ==(_:_:)

**Framework**: Combine  
**Kind**: op

Returns a Boolean value that indicates whether two first publishers have equal upstream publishers.

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
static func == (lhs: Publishers.First<Upstream>, rhs: Publishers.First<Upstream>) -> Bool
```

#### Return Value

`true` if the two publishers have equal upstream publishers; otherwise `false`.

## Parameters

- `lhs`: A drop publisher to compare for equality.
- `rhs`: Another drop publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/first/==(_:_:))*