# *(_:_:)

**Framework**: Swift  
**Kind**: op

Multiplies two values and produces their product.

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
static func * (lhs: Int16, rhs: Int16) -> Int16
```

#### Discussion

The multiplication operator (`*`) calculates the product of its two arguments. For example:

```swift
2 * 3                   // 6
100 * 21                // 2100
-10 * 15                // -150
3.5 * 2.25              // 7.875
```

You cannot use `*` with arguments of different types. To multiply values of different types, convert one of the values to the other value’s type.

```swift
let x: Int8 = 21
let y: Int = 1000000
Int(x) * y              // 21000000
```

The product of the two arguments must be representable in the arguments’ type. In the following example, the result of `21 * 21` is greater than the maximum representable `Int8` value:

```swift
x * 21                  // Overflow error
```

> **Note**: Overflow checking is not performed in `-Ounchecked` builds.

If you want to opt out of overflow checking and wrap the result in case of any overflow, use the overflow multiplication operator (`&*`).

```swift
x &* 21                 // -71
```

## Parameters

- `lhs`: The first value to multiply.
- `rhs`: The second value to multiply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/*(_:_:))*