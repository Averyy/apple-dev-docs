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
static func == (lhs: Just<Output>, rhs: Just<Output>) -> Bool
```

#### Return Value

`true` if the publishers have equal `output` properties; otherwise `false`.

## Parameters

- `lhs`: A   publisher to compare for equality.
- `rhs`: Another   publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/==(_:_:))*