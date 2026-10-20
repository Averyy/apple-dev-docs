# insertSections(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts new sections at the specified indexes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func insertSections(_ sections: IndexSet)
```

```objc
- (void) insertSections:(NSIndexSet *) sections;
```

#### Discussion

Use this method to insert one or more sections into the collection view. This method adds the sections, and it is up to your data source to report the number of items in each section when asked for the information. The collection view then uses that information to get updated layout attributes for the newly inserted sections and items. If the insertions cause a change in the collection view’s visible content, those changes are animated into place.

You can also call this method from a block passed to the [`performBatchUpdates(_:completion:)`](./performbatchupdates%28_,completion%29.md) method when you want to animate multiple separate changes into place at the same time. See the description of that method for more information.

## Parameters

- `sections`: An index set containing the indexes of the sections you want to insert. This parameter must not be `nil`.

## See Also

### Inserting, moving, and deleting sections
- [func moveSection(Int, toSection: Int)](./movesection%28_,tosection%29.md)
  Moves a section from one location to another in the collection view.
- [func deleteSections(IndexSet)](./deletesections%28_%29.md)
  Deletes the sections at the specified indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/insertsections(_:))*