# insertSections(_:)

**Framework**: UIKit  
**Kind**: method

Inserts new sections at the specified indexes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertSections(_ sections: IndexSet)
```

#### Discussion

Use this method to insert one or more sections into the collection view. This method adds the sections, and it is up to your data source to report the number of items in each section when asked for the information. The collection view then uses that information to get updated layout attributes for the newly inserted sections and items. If the insertions cause a change in the collection view’s visible content, those changes are animated into place.

You can also call this method from a block passed to the [`performBatchUpdates(_:completion:)`](uicollectionview/performbatchupdates(_:completion:).md) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## Parameters

- `sections`: An index set containing the indexes of the sections you want to insert. This parameter must not be  .

## See Also

- [func moveSection(Int, toSection: Int)](uicollectionview/movesection(_:tosection:).md)
  Moves a section from one location to another in the collection view.
- [func deleteSections(IndexSet)](uicollectionview/deletesections(_:).md)
  Deletes the sections at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/insertsections(_:))*