# accessibilityHeaderElements(forRow:)

**Framework**: UIKit  
**Kind**: method

Returns the accessibility element for the specified row header.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func accessibilityHeaderElements(forRow row: Int) -> [any UIAccessibilityContainerDataTableCell]?
```

#### Return Value

The accessibility elements for the specified row header.

## Parameters

- `row`: The index of the row containing the header.

## See Also

- [func accessibilityHeaderElements(forColumn: Int) -> [any UIAccessibilityContainerDataTableCell]?](uiaccessibilitycontainerdatatable/accessibilityheaderelements(forcolumn:).md)
  Returns the accessibility element for the specified column header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forrow:))*