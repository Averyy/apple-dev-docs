# alignment(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the alignment of the column, applying to both its column header label and the row view content for that column.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func alignment(_ alignment: TableColumnAlignment) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
```

## Parameters

- `alignment`: The alignment to apply to the column.

## See Also

- [func customizationID(String) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/customizationid(_:).md)
  Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [func defaultVisibility(Visibility) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/defaultvisibility(_:).md)
  Sets the default visibility of a table column.
- [func disabledCustomizationBehavior(TableColumnCustomizationBehavior) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/disabledcustomizationbehavior(_:).md)
  Sets the disabled customization behavior for a table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncontent/alignment(_:))*