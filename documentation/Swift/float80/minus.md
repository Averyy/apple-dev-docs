# -(_:)

**Framework**: Swift  
**Kind**: op

Returns the additive inverse of the specified value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func - (operand: Self) -> Self
```

#### Return Value

The additive inverse of this value.

#### Discussion

The negation operator (prefix `-`) returns the additive inverse of its argument.

```swift
let x = 21
let y = -x
// y == -21
```

The resulting value must be representable in the same type as the argument. In particular, negating a signed, fixed-width integer type’s minimum results in a value that cannot be represented.

```swift
let z = -Int8.min
// Overflow error
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/-(_:)-37tqf)*