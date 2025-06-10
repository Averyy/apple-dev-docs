# init(forCellWith:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a layout attributes object that represents a cell with the specified index path.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(forCellWith indexPath: IndexPath)
```

#### Return Value

A new layout attributes object whose precise type matches the type of the class used to call this method.

#### Discussion

Use this method to create a layout attributes object for a cell in the collection view. Cells are the main type of view presented by a collection view. The index path for a cell typically includes both a section index and an item index for locating the cell’s contents in the collection view’s data source.

## Parameters

- `indexPath`: The index path of the cell.

## See Also

- [convenience init(forSupplementaryViewOfKind: String, with: IndexPath)](uicollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:).md)
  Creates and returns a layout attributes object that represents the specified supplementary view.
- [convenience init(forDecorationViewOfKind: String, with: IndexPath)](uicollectionviewlayoutattributes/init(fordecorationviewofkind:with:).md)
  Creates and returns a layout attributes object that represents the specified decoration view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/init(forcellwith:))*