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
static func == (lhs: Empty<Output, Failure>, rhs: Empty<Output, Failure>) -> Bool
```

#### Return Value

`true` if the two publishers have equal `completeImmediately` properties; otherwise `false`.

## Parameters

- `lhs`: An   instance to compare.
- `rhs`: Another   instance to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/empty/==(_:_:))*