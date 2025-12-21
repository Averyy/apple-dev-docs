# isPositive

**Framework**: Foundation  
**Kind**: property

Controls whether the format input is formatted as a positive or negative range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var isPositive: Bool
```

#### Discussion

When the range is formatted as a positive value, the returned string describes the time from `lowerBound` to `upperBound`. When `isPositive` is set to `false`, the returned string describes the time from `upperBound` to `lowerBound`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/componentsformatstyle/ispositive)*