# show(length:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Returns display strategy that shows leading fields whose value is zero, with a given number of digits.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func show(length: Int) -> Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy
```

## Parameters

- `length`: The number of digits to show for zero-value units.

## See Also

### Using common strategies
- [static var hide: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](./hide.md)
  A display strategy that hides leading fields whose value is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy/show(length:))*