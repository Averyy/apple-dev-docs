# accessibilityDataTableCellElement(forRow:column:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the accessibility element for the specified cell.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func accessibilityDataTableCellElement(forRow row: Int, column: Int) -> (any UIAccessibilityContainerDataTableCell)?
```

#### Return Value

The accessibility element for the cell.

## Parameters

- `row`: The row of the cell.
- `column`: The column of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilitydatatablecellelement(forrow:column:))*