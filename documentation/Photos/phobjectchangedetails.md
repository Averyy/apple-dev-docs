# PHObjectChangeDetails

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A description of changes that occurred in an asset or collection object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHObjectChangeDetails<ObjectType> where ObjectType : PHObject
```

```objc
@interface PHObjectChangeDetails : NSObject
```

## Overview

A [`PHObjectChangeDetails`](./phobjectchangedetails.md) object provides detailed information about differences between two states of an asset or collection object—one that you previously obtained and an updated state that would result if you fetched that entity again. You observe changes by adopting the [`PHPhotoLibraryChangeObserver`](./phphotolibrarychangeobserver.md) protocol and registering your observer with the shared [`PHPhotoLibrary`](./phphotolibrary.md) object. When Photos notifies your observer of a change, you get change details by passing the object you’re interested in to the [`changeDetailsForObject:`](./phchange/changedetailsforobject_.md) method.

For an asset collection or collection list, a [`PHObjectChangeDetails`](./phobjectchangedetails.md) object describe changes only to the collection’s properties. If you’re instead interested in changes to the collection’s membership, fetch the collection’s contents and use the [`changeDetails(for:)`](./phchange/changedetails%28for%29-33a6n.md) method to track changes to the fetch result.

> ⚠️ **Warning**:  Don’t map [`changedIndexes`](./phfetchresultchangedetails/changedindexes.md) directly to [`UICollectionView`](../UIKit/uicollectionview.md) item indices in batch updates. Use these indices to reconfigure the corresponding cells after [`performBatchUpdates(_:completion:)`](../UIKit/uicollectionview/performbatchupdates%28_,completion%29.md). [`UICollectionView`](../UIKit/uicollectionview.md) and [`UITableView`](../UIKit/uitableview.md) expect the [`changedIndexes`](./phfetchresultchangedetails/changedindexes.md) to be in the *before* state, while PhotoKit provides them in the *after* state, resulting in a crash if your app performs insertions and deletions at the same time as the changes.

## Topics

### Getting the Changed Object
- [var objectBeforeChanges: ObjectType](./phobjectchangedetails/objectbeforechanges.md)
  An object that reflects the original state of the asset or collection it represents.
- [var objectAfterChanges: ObjectType?](./phobjectchangedetails/objectafterchanges.md)
  An object that reflects the current state of the asset or collection it represents.
### Getting Change Information
- [var assetContentChanged: Bool](./phobjectchangedetails/assetcontentchanged.md)
  A Boolean value that indicates whether the asset’s photo or video content has changed.
- [var objectWasDeleted: Bool](./phobjectchangedetails/objectwasdeleted.md)
  A Boolean value that indicates whether the object has been deleted from the Photos library.

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
- [class PHFetchResultChangeDetails](./phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobjectchangedetails)*