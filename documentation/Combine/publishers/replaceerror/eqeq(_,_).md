# ==(_:_:)

**Framework**: Combine  
**Kind**: op  
**Role**: Operator

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
static func == (lhs: Publishers.ReplaceError<Upstream>, rhs: Publishers.ReplaceError<Upstream>) -> Bool
```

Available when `Upstream` conforms to `Publisher`, `Upstream` conforms to `Equatable`, and `Upstream.Output` conforms to `Equatable`.

## Return Value

`true` if the two publishers have equal upstream publishers and output elements; otherwise `false`.

## Parameters

- `lhs`: A replace error publisher to compare for equality.
- `rhs`: Another replace error publisher to compare for equality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceerror/==(_:_:))*