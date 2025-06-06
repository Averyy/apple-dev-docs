# init(signOf:magnitudeOf:)

**Framework**: Swift  
**Kind**: init

Creates a new floating-point value using the sign of one value and the magnitude of another.

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
init(signOf: Self, magnitudeOf: Self)
```

#### Discussion

The following example uses this initializer to create a new `Double` instance with the sign of `a` and the magnitude of `b`:

```swift
let a = -21.5
let b = 305.15
let c = Double(signOf: a, magnitudeOf: b)
print(c)
// Prints "-305.15"
```

This initializer implements the IEEE 754 `copysign` operation.

## Parameters

- `signOf`: A value from which to use the sign. The result of the   initializer has the same sign as  .
- `magnitudeOf`: A value from which to use the magnitude. The result of   the initializer has the same magnitude as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(signof:magnitudeof:)-6i9uy)*