# init(forSupplementaryViewOfKind:with:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a layout attributes object that represents the specified supplementary view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(forSupplementaryViewOfKind elementKind: String, with indexPath: IndexPath)
```

#### Return Value

A new layout attributes object whose precise type matches the type of the class used to call this method.

#### Discussion

Use this method to create a layout attributes object for a supplementary view in the collection view. Like cells, supplementary views present data that is managed by the collection view’s data source. But unlike cells, supplementary views are typically designed for a special purpose. For example, header and footer views are laid out differently than cells and can be provided for individual sections or for the collection view as a whole.

It is up to you to decide how to use the `indexPath` parameter to identify a given supplementary view. Typically, you use the `elementKind` parameter to identify the type of the supplementary view and the `indexPath` information to distinguish between different instances of that view.

## Parameters

- `elementKind`: A string that identifies the type of supplementary view.
- `indexPath`: The index path of the view.

## See Also

- [convenience init(forCellWith: IndexPath)](uicollectionviewlayoutattributes/init(forcellwith:).md)
  Creates and returns a layout attributes object that represents a cell with the specified index path.
- [convenience init(forDecorationViewOfKind: String, with: IndexPath)](uicollectionviewlayoutattributes/init(fordecorationviewofkind:with:).md)
  Creates and returns a layout attributes object that represents the specified decoration view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:))*