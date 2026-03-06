# +(_:_:)

**Framework**: Swift  
**Kind**: op

Adds two values and produces their sum.

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
static func + (a: UInt128, b: UInt128) -> UInt128
```

#### Discussion

The addition operator (`+`) calculates the sum of its two arguments. For example:

```swift
1 + 2                   // 3
-10 + 15                // 5
-15 + -5                // -20
21.5 + 3.25             // 24.75
```

You cannot use `+` with arguments of different types. To add values of different types, convert one of the values to the other value’s type.

```swift
let x: Int8 = 21
let y: Int = 1000000
Int(x) + y              // 1000021
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/+(_:_:))*