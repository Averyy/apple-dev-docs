# ~=(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

Returns a Boolean value indicating whether two arguments match by value equality.

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
func ~= <T>(a: T, b: T) -> Bool where T : Equatable
```

#### Discussion

The pattern-matching operator (`~=`) is used internally in `case` statements for pattern matching. When you match against an `Equatable` value in a `case` statement, this operator is called behind the scenes.

```swift
let weekday = 3
let lunch: String
switch weekday {
case 3:
    lunch = "Taco Tuesday!"
default:
    lunch = "Pizza again."
}
// lunch == "Taco Tuesday!"
```

In this example, the `case 3` expression uses this pattern-matching operator to test whether `weekday` is equal to the value `3`.

> **Note**: In most cases, you should use the equal-to operator (`==`) to test whether two instances are equal. The pattern-matching operator is primarily intended to enable `case` statement pattern matching.

## Parameters

- `a`: A value to compare.
- `b`: Another value to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/~=(_:_:))*