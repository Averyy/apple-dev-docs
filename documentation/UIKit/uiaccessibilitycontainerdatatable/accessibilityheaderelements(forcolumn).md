# accessibilityHeaderElements(forColumn:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the accessibility element for the specified column header.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func accessibilityHeaderElements(forColumn column: Int) -> [any UIAccessibilityContainerDataTableCell]?
```

```objc
- (NSArray<id<UIAccessibilityContainerDataTableCell>> *) accessibilityHeaderElementsForColumn:(NSUInteger) column;
```

## Return Value

The accessibility elements for the specified column header.

## Parameters

- `column`: The index of the column containing the header.

## See Also

### Providing header elements
- [func accessibilityHeaderElements(forRow: Int) -> [any UIAccessibilityContainerDataTableCell]?](./accessibilityheaderelements%28forrow%29.md)
  Returns the accessibility element for the specified row header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable/accessibilityheaderelements(forcolumn:))*