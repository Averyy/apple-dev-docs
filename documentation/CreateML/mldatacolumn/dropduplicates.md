# dropDuplicates()

**Framework**: Create ML  
**Kind**: method

Creates a subset of the column by removing all duplicate elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func dropDuplicates() -> MLDataColumn<Element>
```

#### Return Value

A new column.

#### Discussion

> **Note**: The new column may not preserve the order of the original column.

The new column may not preserve the order of the original column.

## See Also

- [func dropMissing() -> MLDataColumn<Element>](mldatacolumn/dropmissing.md)
  Creates a subset of the column by removing all elements without a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn/dropduplicates())*