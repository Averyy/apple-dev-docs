# -(_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator  
**Required**: Yes

Calculates the additive inverse of a value.

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
override static func - (operand: Self) -> Self
```

#### Discussion

The unary minus operator (prefix `-`) calculates the negation of its operand. The result is always exact.

```swift
let x = 21.5
let y = -x
// y == -21.5
```

## Parameters

- `operand`: The value to negate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/-(_:))*