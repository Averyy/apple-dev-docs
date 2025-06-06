# ~=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether an argument matches `nil`.

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
static func ~= (lhs: _OptionalNilComparisonType, rhs: borrowing Wrapped?) -> Bool
```

#### Discussion

You can use the pattern-matching operator (`~=`) to test whether an optional instance is `nil` even when the wrapped value’s type does not conform to the `Equatable` protocol. The pattern-matching operator is used internally in `case` statements for pattern matching.

The following example declares the `stream` variable as an optional instance of a hypothetical `DataStream` type, and then uses a `switch` statement to determine whether the stream is `nil` or has a configured value. When evaluating the `nil` case of the `switch` statement, this operator is called behind the scenes.

```swift
var stream: DataStream? = nil
switch stream {
case nil:
    print("No data stream is configured.")
case let x?:
    print("The data stream has \(x.availableBytes) bytes available.")
}
// Prints "No data stream is configured."
```

> **Note**: To test whether an instance is `nil` in an `if` statement, use the equal-to operator (`==`) instead of the pattern-matching operator. The pattern-matching operator is primarily intended to enable `case` statement pattern matching.

To test whether an instance is `nil` in an `if` statement, use the equal-to operator (`==`) instead of the pattern-matching operator. The pattern-matching operator is primarily intended to enable `case` statement pattern matching.

## Parameters

- `lhs`: A   literal.
- `rhs`: A value to match against  .

## See Also

- [static func == (borrowing Wrapped?, _OptionalNilComparisonType) -> Bool](optional/==(_:_:)-5uee5.md)
  Returns a Boolean value indicating whether the left-hand-side argument is `nil`.
- [static func == (_OptionalNilComparisonType, borrowing Wrapped?) -> Bool](optional/==(_:_:)-6ztpi.md)
  Returns a Boolean value indicating whether the right-hand-side argument is `nil`.
- [static func != (borrowing Wrapped?, _OptionalNilComparisonType) -> Bool](optional/!=(_:_:)-38b38.md)
  Returns a Boolean value indicating whether the left-hand-side argument is not `nil`.
- [static func != (_OptionalNilComparisonType, borrowing Wrapped?) -> Bool](optional/!=(_:_:)-6xpzw.md)
  Returns a Boolean value indicating whether the right-hand-side argument is not `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/~=(_:_:))*