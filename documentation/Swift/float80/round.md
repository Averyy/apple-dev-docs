# round(_:)

**Framework**: Swift  
**Kind**: method

Rounds the value to an integral value using the specified rounding rule.

**Availability**:
- macOS 10.10+

## Declaration

```swift
mutating func round(_ rule: FloatingPointRoundingRule)
```

#### Discussion

The following example rounds a value using four different rounding rules:

```swift
// Equivalent to the C 'round' function:
var w = 6.5
w.round(.toNearestOrAwayFromZero)
// w == 7.0

// Equivalent to the C 'trunc' function:
var x = 6.5
x.round(.towardZero)
// x == 6.0

// Equivalent to the C 'ceil' function:
var y = 6.5
y.round(.up)
// y == 7.0

// Equivalent to the C 'floor' function:
var z = 6.5
z.round(.down)
// z == 6.0
```

For more information about the available rounding rules, see the `FloatingPointRoundingRule` enumeration. To round a value using the default “schoolbook rounding” of `.toNearestOrAwayFromZero`, you can use the shorter `round()` method instead.

```swift
var w1 = 6.5
w1.round()
// w1 == 7.0
```

## Parameters

- `rule`: The rounding rule to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/round(_:))*