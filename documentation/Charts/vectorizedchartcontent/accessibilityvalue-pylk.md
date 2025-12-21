# accessibilityValue(_:)

**Framework**: Swift Charts  
**Kind**: method

Adds a description of the value that the chart content contains.

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
func accessibilityValue(_ valueDescription: KeyPath<Self.DataElement, Text>) -> some VectorizedChartContent<Self.DataElement>
```

## See Also

- [func accessibilityHidden(KeyPath<Self.DataElement, Bool>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilityhidden(_:).md)
  Specifies whether to hide this chart content from system accessibility features.
- [func accessibilityIdentifier(KeyPath<Self.DataElement, String>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilityidentifier(_:).md)
  Adds an identifier string to the chart content.
- [func accessibilityLabel(KeyPath<Self.DataElement, LocalizedStringKey>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilitylabel(_:)-5r0pw.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityLabel(KeyPath<Self.DataElement, some StringProtocol>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilitylabel(_:)-8zoay.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityLabel(KeyPath<Self.DataElement, Text>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilitylabel(_:)-46jbt.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityValue(KeyPath<Self.DataElement, some StringProtocol>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilityvalue(_:)-2rv8b.md)
  Adds a description of the value that the chart content contains.
- [func accessibilityValue(KeyPath<Self.DataElement, LocalizedStringKey>) -> some VectorizedChartContent<Self.DataElement>
](vectorizedchartcontent/accessibilityvalue(_:)-3dei8.md)
  Adds a description of the value that the chart content contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent/accessibilityvalue(_:)-pylk)*