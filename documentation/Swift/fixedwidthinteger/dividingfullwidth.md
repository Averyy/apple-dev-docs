# dividingFullWidth(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns a tuple containing the quotient and remainder obtained by dividing the given value by this value.

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
func dividingFullWidth(_ dividend: (high: Self, low: Self.Magnitude)) -> (quotient: Self, remainder: Self)
```

#### Return Value

A tuple containing the quotient and remainder obtained by dividing `dividend` by this value.

#### Discussion

The resulting quotient must be representable within the bounds of the type. If the quotient is too large to represent in the type, a runtime error may occur.

The following example divides a value that is too large to be represented using a single `Int` instance by another `Int` value. Because the quotient is representable as an `Int`, the division succeeds.

```swift
// 'dividend' represents the value 0x506f70652053616e74612049494949
let dividend = (22640526660490081, 7959093232766896457 as UInt)
let divisor = 2241543570477705381

let (quotient, remainder) = divisor.dividingFullWidth(dividend)
// quotient == 186319822866995413
// remainder == 0
```

## Parameters

- `dividend`: A tuple containing the high and low parts of a   double-width integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/fixedwidthinteger/dividingfullwidth(_:))*