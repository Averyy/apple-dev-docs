# accessibilityHeaderElements(forRow:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the accessibility element for the specified row header.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func accessibilityHeaderElements(forRow row: Int) -> [any UIAccessibilityContainerDataTableCell]?
```

```objc
- (NSArray<id<UIAccessibilityContainerDataTableCell>> *) accessibilityHeaderElementsForRow:(NSUInteger) row;
```

## Return Value

The accessibility elements for the specified row header.

## Parameters

- `row`: The index of the row containing the header.

## See Also

### Providing header elements
- [func accessibilityHeaderElements(forColumn: Int) -> [any UIAccessibilityContainerDataTableCell]?](./accessibilityheaderelements%28forcolumn%29.md)
  Returns the accessibility element for the specified column header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forrow:))*