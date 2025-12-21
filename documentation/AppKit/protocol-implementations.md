# Protocol Implementations

**Framework**: AppKit

Access the diffable data source’s implementations of protocol methods.

#### Overview

The diffable data source type conforms to several protocols, including [`NSCollectionViewDataSource`](nscollectionviewdatasource.md) and [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable). This page lists the diffable data source type’s implementations of those protocol requirements.

## Topics

### Getting Item and Section Metrics
- [func collectionView(NSCollectionView, numberOfItemsInSection: Int) -> Int](nscollectionviewdatasource/collectionview(_:numberofitemsinsection:).md)
  Asks your data source object to provide the number of items in the specified section.
- [func numberOfSections(in: NSCollectionView) -> Int](nscollectionviewdatasource/numberofsections(in:).md)
  Asks your data source object to provide the total number of sections.
### Getting Views for Items
- [func collectionView(NSCollectionView, itemForRepresentedObjectAt: IndexPath) -> NSCollectionViewItem](nscollectionviewdatasource/collectionview(_:itemforrepresentedobjectat:).md)
  Asks your data source object to provide the item at the specified location in the collection view.
- [func collectionView(NSCollectionView, viewForSupplementaryElementOfKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSView](nscollectionviewdatasource/collectionview(_:viewforsupplementaryelementofkind:at:).md)
  Asks your data source object to provide the supplementary view at the specified location in a section of the collection view.
### Debugging a Diffable Data Source
- [func description() -> String](nscollectionviewdiffabledatasource-axww/description.md)
  Returns a string with a description of the diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/protocol-implementations)*