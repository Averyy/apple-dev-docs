# numericCast(_:)

**Framework**: Swift  
**Kind**: func

Returns the given integer as the equivalent value in a different integer type.

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
func numericCast<T, U>(_ x: T) -> U where T : BinaryInteger, U : BinaryInteger
```

#### Return Value

The value of `x` converted to type `U`.

#### Discussion

Calling the `numericCast(_:)` function is equivalent to calling an initializer for the destination type. `numericCast(_:)` traps on overflow in `-O` and `-Onone` builds.

## Parameters

- `x`: The integer to convert, an instance of type  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/numericcast(_:))*