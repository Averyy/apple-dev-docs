# PHPhotoLibraryChangeObserver

**Framework**: Photos  
**Kind**: protocol  
**Role**: Protocol

A protocol to adopt to have the system notify your app of changes to the photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol PHPhotoLibraryChangeObserver : NSObjectProtocol
```

```objc
@protocol PHPhotoLibraryChangeObserver <NSObject>
```

## Mentions

- [Observing Changes in the Photo Library](../PhotoKit/observing-changes-in-the-photo-library.md)

## Overview

The [`PHPhotoLibraryChangeObserver`](./phphotolibrarychangeobserver.md) protocol notifies you of changes that occur in the photo library, regardless of whether those changes are made by your app, by a user in the Photos app, or by another app that uses the Photos framework. To receive change messages, register your observer with the [`register(_:)`](./phphotolibrary/register%28_%29-6y3b9.md) method. For any assets or collections that you fetch, Photos sends change messages whenever those assets or collections change. Use this protocol to track changes across multiple parts of your app or respond to changes made in another app or extension.

### Handling Changes: An Example

The example code below shows how you might implement this protocol in a view controller that uses a [`UICollectionView`](../UIKit/uicollectionview.md) interface to display the contents of an album. The view controller keeps a reference to the [`PHAssetCollection`](./phassetcollection.md) object representing the displayed album and the [`PHFetchResult`](./phfetchresult.md) object (returned by the [`fetchAssets(in:options:)`](./phasset/fetchassets%28in,options%29.md) method) listing the album’s contents. Then, in its [`photoLibraryDidChange(_:)`](./phphotolibrarychangeobserver/photolibrarydidchange%28_%29.md) method, the view controller checks for differences between the objects it fetched and the new state of the photo library, and updates its collection view accordingly.

**Swift**:

```swift
func photoLibraryDidChange(_ changeInstance: PHChange) {
    guard let collectionView = self.collectionView else { return }
    // Change notifications may be made on a background queue.
    // Re-dispatch to the main queue to update the UI.
    DispatchQueue.main.sync {
        // Check for changes to the displayed album itself
        // (its existence and metadata, not its member assets).
        if let albumChanges = changeInstance.changeDetails(for: assetCollection) {
            // Fetch the new album and update the UI accordingly.
            assetCollection = albumChanges.objectAfterChanges! as! PHAssetCollection
            navigationController?.navigationItem.title = assetCollection.localizedTitle
        }
        // Check for changes to the list of assets (insertions, deletions, moves, or updates).
        if let changes = changeInstance.changeDetails(for: fetchResult) {
            // Keep the new fetch result for future use.
            fetchResult = changes.fetchResultAfterChanges
            if changes.hasIncrementalChanges {
                // If there are incremental diffs, animate them in the collection view.
                collectionView.performBatchUpdates({
                    // For indexes to make sense, updates must be in this order:
                    // delete, insert, reload, move.
                    if let removed = changes.removedIndexes where removed.count > 0 {
                        collectionView.deleteItems(at: removed.map { IndexPath(item: $0, section:0) })
                    }
                    if let inserted = changes.insertedIndexes where inserted.count > 0 {
                        collectionView.insertItems(at: inserted.map { IndexPath(item: $0, section:0) })
                    }
                    if let changed = changes.changedIndexes where changed.count > 0 {
                        collectionView.reloadItems(at: changed.map { IndexPath(item: $0, section:0) })
                    }
                    changes.enumerateMoves { fromIndex, toIndex in
                        collectionView.moveItem(at: IndexPath(item: fromIndex, section: 0),
                                                to: IndexPath(item: toIndex, section: 0))
                    }
                })
            } else {
                // Reload the collection view if incremental diffs aren't available.
                collectionView.reloadData()
            }
        }
    }
}
```

**Objective-C**:

```objc
- (void)photoLibraryDidChange:(PHChange *)changeInfo {
    // Change notifications may be made on a background queue.
    // Re-dispatch to the main queue to update the UI.
    dispatch_async(dispatch_get_main_queue(), ^{
        // Check for changes to the displayed album itself
        // (its existence and metadata, not its member assets).
        PHObjectChangeDetails *albumChanges = [changeInfo changeDetailsForObject:self.displayedAlbum];
        if (albumChanges) {
            // Fetch the new album and update the UI accordingly.
            self.displayedAlbum = [albumChanges objectAfterChanges];
            self.navigationController.navigationItem.title = self.displayedAlbum.localizedTitle;
        }
 
        // Check for changes to the list of assets (insertions, deletions, moves, or updates).
        PHFetchResultChangeDetails *collectionChanges = [changeInfo changeDetailsForFetchResult:self.albumContents];
        if (collectionChanges) {
            // Keep the new fetch result for future use.
            self.albumContents = collectionChanges.fetchResultAfterChanges;
 
            if (collectionChanges.hasIncrementalChanges)  {
                // If there are incremental diffs, animate them in the collection view.
                [self.collectionView performBatchUpdates:^{
                    NSIndexSet *removed = collectionChanges.removedIndexes;
                    if (removed.count) {
                        [self.collectionView deleteItemsAtIndexPaths:[self indexPathsFromIndexSet:removed]];
                    }
                    NSIndexSet *inserted = collectionChanges.insertedIndexes;
                    if (inserted.count) {
                        [self.collectionView insertItemsAtIndexPaths:[self indexPathsFromIndexSet:inserted]];
                    }
                    NSIndexSet *changed = collectionChanges.changedIndexes;
                    if (changed.count) {
                        [self.collectionView reloadItemsAtIndexPaths:[self indexPathsFromIndexSet:changed]];
                    }
                    if (collectionChanges.hasMoves) {
                        [collectionChanges enumerateMovesWithBlock:^(NSUInteger fromIndex, NSUInteger toIndex) {
                            NSIndexPath *fromIndexPath = [NSIndexPath indexPathForItem:fromIndex inSection:0];
                            NSIndexPath *toIndexPath = [NSIndexPath indexPathForItem:toIndex inSection:0];
                            [self.collectionView moveItemAtIndexPath:fromIndexPath toIndexPath:toIndexPath];
                        }];
                    }
                } completion:nil];
            } else {
                // Reload the collection view if incremental diffs aren't available.
                [self.collectionView reloadData];
            }
        }
    });
}
```

## Topics

### Observing Photo Library Changes
- [func photoLibraryDidChange(PHChange)](./phphotolibrarychangeobserver/photolibrarydidchange%28_%29.md)
  Tells your observer that a set of changes has occurred in the Photos library.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing Library Changes
- [Observing Changes in the Photo Library](../PhotoKit/observing-changes-in-the-photo-library.md)
  Register an observer to be notified of changes to the photo library.
- [func register(any PHPhotoLibraryChangeObserver)](./phphotolibrary/register%28_%29-6y3b9.md)
  Registers an object to receive messages when objects in the photo library change.
- [func unregisterChangeObserver(any PHPhotoLibraryChangeObserver)](./phphotolibrary/unregisterchangeobserver%28_%29.md)
  Unregisters an object so that it no longer receives change messages.
- [class PHChange](./phchange.md)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](./phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](./phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver)*