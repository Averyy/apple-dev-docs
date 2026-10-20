# init(attributedTitle:range:gridlinePositions:valueDescriptionProvider:)

**Framework**: Accessibility  
**Kind**: init  
**Role**: Initializer

Creates a numeric data axis with the specified attributed title, range, gridline positions, and value description provider closure.

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
convenience init(attributedTitle: NSAttributedString, range: ClosedRange<Double>, gridlinePositions: [Double], valueDescriptionProvider: @escaping (Double) -> String)
```

## See Also

### Creating a numeric data axis
- [convenience init(title: String, range: ClosedRange<Double>, gridlinePositions: [Double], valueDescriptionProvider: (Double) -> String)](./init%28title,range,gridlinepositions,valuedescriptionprovider%29.md)
  Creates a numeric data axis with the specified title, range, gridline positions, and value description provider closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor/init(attributedtitle:range:gridlinepositions:valuedescriptionprovider:))*