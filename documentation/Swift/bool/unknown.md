# ||(_:_:)

**Framework**: Swift  
**Kind**: op

Performs a logical OR operation on two Boolean values.

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
static func || (lhs: Bool, rhs: @autoclosure () throws -> Bool) rethrows -> Bool
```

#### Discussion

The logical OR operator (`||`) combines two Boolean values and returns `true` if at least one of the values is `true`. If both values are `false`, the operator returns `false`.

This operator uses short-circuit evaluation: The left-hand side (`lhs`) is evaluated first, and the right-hand side (`rhs`) is evaluated only if `lhs` evaluates to `false`. For example:

```swift
let majorErrors: Set = ["No first name", "No last name", ...]
let error = ""

if error.isEmpty || !majorErrors.contains(error) {
    print("No major errors detected")
} else {
    print("Major error: \(error)")
}
// Prints "No major errors detected"
```

In this example, `lhs` tests whether `error` is an empty string. Evaluation of the `||` operator is one of the following:

- When `error` is an empty string, `lhs` evaluates to `true` and `rhs` is not evaluated, skipping the call to `majorErrors.contains(_:)`. The result of the operation is `true`.
- When `error` is not an empty string, `lhs` evaluates to `false` and `rhs` is evaluated. The result of evaluating `rhs` is the result of the `||` operation.

## Parameters

- `lhs`: The left-hand side of the operation.
- `rhs`: The right-hand side of the operation.

## See Also

- [func toggle()](bool/toggle.md)
  Toggles the Boolean variable’s value.
- [static func ! (Bool) -> Bool](bool/!(_:).md)
  Performs a logical NOT operation on a Boolean value.
- [static func && (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](bool/&&(_:_:).md)
  Performs a logical AND operation on two Boolean values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool/__(_:_:))*