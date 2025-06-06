# velocity(at:)

**Framework**: SwiftUI  
**Kind**: method

Returns the rate of change (first derivative) of the output value of the curve at the given time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func velocity(at progress: Double) -> Double
```

#### Return Value

The velocity of the output value (y component) of the curve at the given time.

## Parameters

- `progress`: The input progress (x component). The provided value is   clamped to the range [0,1].

## See Also

- [func value(at: Double) -> Double](unitcurve/value(at:).md)
  Returns the output value (y component) of the curve at the given time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unitcurve/velocity(at:))*