# PHFetchResultChangeDetails

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A description of changes that occurred in the set of asset or collection objects listed in a fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHFetchResultChangeDetails<ObjectType> where ObjectType : PHObject
```

```objc
@interface PHFetchResultChangeDetails : NSObject
```

#### Overview

A [`PHFetchResultChangeDetails`](./phfetchresultchangedetails.md) object provides detailed information about the differences between two fetch results—one that you previously obtained and an updated one that would result if you performed the same fetch again. The change details object provides information useful for updating a UI that lists the contents of a fetch result, such as the indexes of added, removed, and rearranged objects.

##### Processing Changes in Order

PhotoKit describes [`changedIndexes`](./phfetchresultchangedetails/changedindexes.md) in the *after* state, while [`UICollectionView`](../UIKit/uicollectionview.md)w’s [`performBatchUpdates(_:completion:)`](../UIKit/uicollectionview/performbatchupdates%28_,completion%29.md) expects them in the *before* state. As a result, [`changedIndexes`](./phfetchresultchangedetails/changedindexes.md) can’t be used safely inside [`performBatchUpdates(_:completion:)`](../UIKit/uicollectionview/performbatchupdates%28_,completion%29.md).

Instead, use [`changedIndexes`](./phfetchresultchangedetails/changedindexes.md) *after* and outside the [`performBatchUpdates(_:completion:)`](../UIKit/uicollectionview/performbatchupdates%28_,completion%29.md) call, reapplying the code used to configure cells in [`cellForItem(at:)`](../UIKit/uicollectionview/cellforitem%28at%29.md) rather than telling [`UICollectionView`](../UIKit/uicollectionview.md) to reload.

**Swift**:

```swift
let collectionView = UICollectionView()
let fetchResultChangeDetails = PHFetchResultChangeDetails()
let deletedCollectionIndicesBeforeChanges = IndexSet()
let insertedCollectionIndicesAfterDeletions = IndexSet()
let deletedPhotoPathsBeforeChanges: [IndexPath] = []
let insertedPhotoPathsAfterDeletions: [IndexPath] = []

collectionView.performBatchUpdates({ () -> Void in
    if (!deletedCollectionIndicesBeforeChanges.isEmpty) {
        collectionView.deleteSections(deletedCollectionIndicesBeforeChanges)
    }
    if (!insertedCollectionIndicesAfterDeletions.isEmpty) {
        collectionView.insertSections(insertedCollectionIndicesAfterDeletions)
    }
    if (!deletedPhotoPathsBeforeChanges.isEmpty) {
        collectionView.deleteItems(at: deletedPhotoPathsBeforeChanges)
    }
    if (!insertedPhotoPathsAfterDeletions.isEmpty) {
        collectionView.insertItems(at: insertedPhotoPathsAfterDeletions)
    }
}, completion:nil)

guard let changeIndices = fetchResultChangeDetails.changedIndexes else {
    return
}
for indexSetElem in changeIndices {
    let indexPath = IndexPath(item: indexSetElem, section: 0)
    guard let changedCell = collectionView.cellForItem(at: indexPath) else {
        break
    }
    // ... Configure changedCell here ...
}
```

**Objective-C**:

```objc
@property (nonatomic, strong) UICollectionView* collectionView;
// ...
PHFetchResultChangeDetails* fetchResultChangeDetails;
NSIndexSet* deletedCollectionIndicesBeforeChanges;
NSIndexSet* insertedCollectionIndicesAfterDeletions;
NSArray* deletedPhotoPathsBeforeChanges;
NSArray* insertedPhotoPathsAfterDeletions;

[self.collectionView performBatchUpdates:^{
    if (deletedCollectionIndicesBeforeChanges.count > 0) {
        [self.collectionView deleteSections:deletedCollectionIndicesBeforeChanges];
    }
    if (insertedCollectionIndicesAfterDeletions.count > 0) {
        [self.collectionView insertSections:insertedCollectionIndicesAfterDeletions];
    }
    if (deletedPhotoPathsBeforeChanges.count > 0) {
        [self.collectionView deleteItemsAtIndexPaths:deletedPhotoPathsBeforeChanges];
    }
    if (insertedPhotoPathsAfterDeletions) {
        [self.collectionView insertItemsAtIndexPaths:insertedPhotoPathsAfterDeletions];
    }
} completion:nil];

[fetchResultChangeDetails.changedIndexes enumerateIndexesUsingBlock:^(NSUInteger index, BOOL* stop) {
    NSIndexPath* indexPath = [NSIndexPath indexPathWithItem:index inSection:0];
    UICollectionViewCell* changedCell = [self.collectionView cellForItemAtIndexPath:indexPath];
    if (changedCell) {
        // ... Configure changedCell here ...
    }
    // Set *stop = YES to stop iteration early.
}];
```

## Topics

### Getting the Changed Fetch Result
- [var fetchResultBeforeChanges: PHFetchResult<ObjectType>](./phfetchresultchangedetails/fetchresultbeforechanges.md)
  The original fetch result, without recent changes.
- [var fetchResultAfterChanges: PHFetchResult<ObjectType>](./phfetchresultchangedetails/fetchresultafterchanges.md)
  The current fetch result, incorporating recent changes.
### Getting Change Information
- [var hasIncrementalChanges: Bool](./phfetchresultchangedetails/hasincrementalchanges.md)
  A Boolean value that indicates whether changes to the fetch result can be described incrementally.
- [var removedIndexes: IndexSet?](./phfetchresultchangedetails/removedindexes.md)
  The indexes from which objects have been removed from the fetch result.
- [var removedObjects: [ObjectType]](./phfetchresultchangedetails/removedobjects.md)
  The items that have been removed from the fetch result.
- [var insertedIndexes: IndexSet?](./phfetchresultchangedetails/insertedindexes.md)
  The indexes where new objects have been inserted in the fetch result.
- [var insertedObjects: [ObjectType]](./phfetchresultchangedetails/insertedobjects.md)
  The new items that have been inserted in the fetch result.
- [var changedIndexes: IndexSet?](./phfetchresultchangedetails/changedindexes.md)
  The indexes of objects in the fetch result whose content or metadata have been updated.
- [var changedObjects: [ObjectType]](./phfetchresultchangedetails/changedobjects.md)
  The objects in the fetch result whose content or metadata have been updated.
- [var hasMoves: Bool](./phfetchresultchangedetails/hasmoves.md)
  A Boolean value that indicates whether objects have been rearranged in the fetch result.
- [func enumerateMoves((Int, Int) -> Void)](./phfetchresultchangedetails/enumeratemoves%28_%29.md)
  Runs the specified block for each case where an object has moved from one index to another in the fetch result.
### Comparing Fetch Results
- [convenience init(from: PHFetchResult<ObjectType>, to: PHFetchResult<ObjectType>, changedObjects: [ObjectType])](./phfetchresultchangedetails/init%28from,to,changedobjects%29.md)
  Creates a change details object that summarizes the differences between two fetch results.
### Initializers
- [convenience init(fromFetchResult: PHFetchResult<ObjectType>, toFetchResult: PHFetchResult<ObjectType>, changedObjects: [ObjectType])](./phfetchresultchangedetails/init%28fromfetchresult,tofetchresult,changedobjects%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Observing Library Changes
- [Observing Changes in the Photo Library](../PhotoKit/observing-changes-in-the-photo-library.md)
  Register an observer to be notified of changes to the photo library.
- [func register(any PHPhotoLibraryChangeObserver)](./phphotolibrary/register%28_%29-6y3b9.md)
  Registers an object to receive messages when objects in the photo library change.
- [func unregisterChangeObserver(any PHPhotoLibraryChangeObserver)](./phphotolibrary/unregisterchangeobserver%28_%29.md)
  Unregisters an object so that it no longer receives change messages.
- [protocol PHPhotoLibraryChangeObserver](./phphotolibrarychangeobserver.md)
  A protocol to adopt to have the system notify your app of changes to the photo library.
- [class PHChange](./phchange.md)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](./phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails)*