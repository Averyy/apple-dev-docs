# -(_:_:)

**Framework**: Swift  
**Kind**: op

Subtracts one value from another and produces their difference.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func - (a: UInt128, b: UInt128) -> UInt128
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/-(_:_:))*