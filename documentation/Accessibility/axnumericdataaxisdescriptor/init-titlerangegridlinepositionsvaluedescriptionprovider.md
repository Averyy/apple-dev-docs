# init(title:range:gridlinePositions:valueDescriptionProvider:)

**Framework**: Accessibility  
**Kind**: init

Creates a numeric data axis with the specified title, range, gridline positions, and value description provider closure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(title: String, range: ClosedRange<Double>, gridlinePositions: [Double], valueDescriptionProvider: @escaping (Double) -> String)
```

## See Also

- [convenience init(attributedTitle: NSAttributedString, range: ClosedRange<Double>, gridlinePositions: [Double], valueDescriptionProvider: (Double) -> String)](axnumericdataaxisdescriptor/init(attributedtitle:range:gridlinepositions:valuedescriptionprovider:).md)
  Creates a numeric data axis with the specified attributed title, range, gridline positions, and value description provider closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor/init(title:range:gridlinepositions:valuedescriptionprovider:))*