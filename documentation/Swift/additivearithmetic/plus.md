# +(_:_:)

**Framework**: Swift  
**Kind**: op  
**Required**: Yes

Adds two values and produces their sum.

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
static func + (lhs: Self, rhs: Self) -> Self
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

## Parameters

- `lhs`: The first value to add.
- `rhs`: The second value to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/additivearithmetic/+(_:_:))*