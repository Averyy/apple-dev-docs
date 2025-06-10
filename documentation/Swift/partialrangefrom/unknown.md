# ~=(_:_:)

**Framework**: Swift  
**Kind**: op

Returns a Boolean value indicating whether a value is included in a range.

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
static func ~= (pattern: Self, value: Self.Bound) -> Bool
```

#### Discussion

You can use the pattern-matching operator (`~=`) to test whether a value is included in a range. The pattern-matching operator is used internally in `case` statements for pattern matching. The following example uses the `~=` operator to test whether an integer is included in a range of single-digit numbers:

```swift
let chosenNumber = 3
if 0..<10 ~= chosenNumber {
    print("\(chosenNumber) is a single digit.")
}
// Prints "3 is a single digit."
```

## Parameters

- `pattern`: A range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialrangefrom/~=(_:_:))*