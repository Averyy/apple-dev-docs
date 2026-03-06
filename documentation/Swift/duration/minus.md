# -(_:_:)

**Framework**: Swift  
**Kind**: op

Subtracts one value from another and produces their difference.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func - (lhs: Duration, rhs: Duration) -> Duration
```

#### Discussion

The subtraction operator (`-`) calculates the difference of its two arguments. For example:

```swift
8 - 3                   // 5
-10 - 5                 // -15
100 - -5                // 105
10.5 - 100.0            // -89.5
```

You cannot use `-` with arguments of different types. To subtract values of different types, convert one of the values to the other value’s type.

```swift
let x: UInt8 = 21
let y: UInt = 1000000
y - UInt(x)             // 999979
```

## Parameters

- `lhs`: A numeric value.
- `rhs`: The value to subtract from `lhs`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/-(_:_:))*