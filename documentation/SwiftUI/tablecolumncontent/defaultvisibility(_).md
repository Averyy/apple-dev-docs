# defaultVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the default visibility of a table column.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func defaultVisibility(_ visibility: Visibility) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
```

#### Discussion

A `hidden` column will not be visible, unless the `Table` is also bound to `TableColumnCustomization` and either modified programmatically or by the user.

## Parameters

- `visibility`: The default visibility to apply to columns.

## See Also

### Configuring the content
- [func alignment(TableColumnAlignment) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](./alignment%28_%29.md)
  Sets the alignment of the column, applying to both its column header label and the row view content for that column.
- [func customizationID(String) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](./customizationid%28_%29.md)
  Sets the identifier to be associated with a column when persisting its state with `TableColumnCustomization`.
- [func disabledCustomizationBehavior(TableColumnCustomizationBehavior) -> some TableColumnContent<Self.TableRowValue, Self.TableColumnSortComparator>
](./disabledcustomizationbehavior%28_%29.md)
  Sets the disabled customization behavior for a table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncontent/defaultvisibility(_:))*