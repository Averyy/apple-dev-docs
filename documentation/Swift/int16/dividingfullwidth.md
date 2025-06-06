# dividingFullWidth(_:)

**Framework**: Swift  
**Kind**: method

Returns a tuple containing the quotient and remainder of dividing the given value by this value.

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
func dividingFullWidth(_ dividend: (high: Int16, low: Int16.Magnitude)) -> (quotient: Int16, remainder: Int16)
```

#### Return Value

A tuple containing the quotient and remainder of `dividend` divided by this value.

#### Discussion

The resulting quotient must be representable within the bounds of the type. If the quotient of dividing `dividend` by this value is too large to represent in the type, a runtime error will occur.

## Parameters

- `dividend`: A tuple containing the high and low parts of a   double-width integer. The   component of the value carries the   sign, if the type is signed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/dividingfullwidth(_:))*