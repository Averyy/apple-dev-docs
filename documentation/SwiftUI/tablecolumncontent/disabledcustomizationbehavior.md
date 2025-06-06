# disabledCustomizationBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the disabled customization behavior for a table column.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func disabledCustomizationBehavior(_ behavior: TableColumnCustomizationBehavior) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
```

#### Discussion

When the containing `Table` is bound to some `TableColumnCustomization`, all columns will be able to be customized by the user on macOS by default (i.e. `TableColumnCustomizationBehavior.all`). This modifier allows disabling specific behavior.

This modifier has no effect on iOS since `Table` does not support any built-in user customization features.

This does not prevent programmatic changes to a table column customization.

## Parameters

- `behavior`: The behavior to disable, or   to not allow   any customization.

## See Also

- [func alignment(TableColumnAlignment) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/alignment(_:).md)
  Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [func customizationID(String) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/customizationid(_:).md)
  Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [func defaultVisibility(Visibility) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](tablecolumncontent/defaultvisibility(_:).md)
  Sets the default visibility of a table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncontent/disabledcustomizationbehavior(_:))*