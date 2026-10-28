# ...(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a closed range that contains both of its bounds.

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
static func ... (minimum: Self, maximum: Self) -> ClosedRange<Self>
```

## Discussion

Use the closed range operator (`...`) to create a closed range of any type that conforms to the `Comparable` protocol. This example creates a `ClosedRange<Character>` from “a” up to, and including, “z”.

```swift
let lowercase = "a"..."z"
print(lowercase.contains("z"))
// Prints "true"
```

> **Precondition**: `minimum <= maximum`.

## Parameters

- `minimum`: The lower bound for the range.
- `maximum`: The upper bound for the range.

## See Also

### Creating a Range Expression
- [static func ... (Self) -> PartialRangeThrough<Self>](./dotdotdot%28_%29-4mm4o.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](./dotdotdot%28_%29-6ct5g.md)
  Returns a partial range extending upward from a lower bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/'...(_:_:))*