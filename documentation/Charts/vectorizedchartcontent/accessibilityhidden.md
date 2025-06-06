# accessibilityHidden(_:)

**Framework**: Swift Charts  
**Kind**: method

Specifies whether to hide this chart content from system accessibility features.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityHidden(_ hidden: KeyPath<Self.DataElement, Bool>) -> some VectorizedChartContent<Self.DataElement>
```

## See Also

- [func accessibilityIdentifier(KeyPath<Self.DataElement, String>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilityidentifier(_:).md)
  Adds an identifier string to the chart content.
- [func accessibilityLabel(KeyPath<Self.DataElement, some StringProtocol>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilitylabel(_:)-8zoay.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityValue(KeyPath<Self.DataElement, some StringProtocol>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilityvalue(_:)-2rv8b.md)
  Adds a description of the value that the chart content contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/accessibilityhidden(_:))*