# rounded(_:)

**Framework**: Swift  
**Kind**: method

Returns this value rounded to an integral value using the specified rounding rule.

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
func rounded(_ rule: FloatingPointRoundingRule) -> Self
```

#### Return Value

The integral value found by rounding using `rule`.

#### Discussion

The following example rounds a value using four different rounding rules:

```swift
let x = 6.5

// Equivalent to the C 'round' function:
print(x.rounded(.toNearestOrAwayFromZero))
// Prints "7.0"

// Equivalent to the C 'trunc' function:
print(x.rounded(.towardZero))
// Prints "6.0"

// Equivalent to the C 'ceil' function:
print(x.rounded(.up))
// Prints "7.0"

// Equivalent to the C 'floor' function:
print(x.rounded(.down))
// Prints "6.0"
```

For more information about the available rounding rules, see the `FloatingPointRoundingRule` enumeration. To round a value using the default “schoolbook rounding” of `.toNearestOrAwayFromZero`, you can use the shorter `rounded()` method instead.

```swift
print(x.rounded())
// Prints "7.0"
```

## Parameters

- `rule`: The rounding rule to use.

## See Also

- [func rounded() -> Self](float/rounded.md)
- [func round()](float/round.md)
- [func round(FloatingPointRoundingRule)](float/round(_:).md)
  Rounds the value to an integral value using the specified rounding rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/rounded(_:))*