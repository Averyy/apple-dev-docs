# customizationID(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func customizationID(_ id: String) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
```

#### Discussion

This is required to allow user customization of a specific table column, in addition to the table as a whole being provided a binding to a `TableColumnCustomization`.

The identifier needs to to be stable, including across app version updates, since it is used to persist the user customization.

## Parameters

- `id`: The identifier to associate with a column.

## See Also

- [func alignment(TableColumnAlignment) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/alignment(_:).md)
  Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [func defaultVisibility(Visibility) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/defaultvisibility(_:).md)
  Sets the default visibility of a table column.
- [func disabledCustomizationBehavior(TableColumnCustomizationBehavior) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/disabledcustomizationbehavior(_:).md)
  Sets the disabled customization behavior for a table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncontent/customizationid(_:))*