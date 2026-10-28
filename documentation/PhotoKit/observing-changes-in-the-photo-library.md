# Observing Changes in the Photo Library

**Framework**: PhotoKit  
**Role**: Article

Register an observer to be notified of changes to the photo library.

## Overview

To be notified of changes to the photo library, use the [`register(_:)`](../Photos/phphotolibrary/register%28_%29-6y3b9.md) method to designate an observer object. Whenever you use a fetch method, such as [`fetchAssets(with:)`](../Photos/phasset/fetchassets%28with%29.md), to retrieve assets or collections, Photos automatically registers your interest in observing changes to those items. After you perform a fetch, Photos sends messages to your observer through the [`PHPhotoLibraryChangeObserver`](../Photos/phphotolibrarychangeobserver.md) protocol whenever the items in the resulting fetch request change. For example, you’ll get notified when changes add items, remove items, or reorder the list of items in the fetch result. Update your user interface based on the details you receive from [`PHChange`](../Photos/phchange.md) objects.

Use the shared [`PHPhotoLibrary`](../Photos/phphotolibrary.md) object to register a change handler for the assets and collections you fetch. Photos tells your app whenever another app or device changes the content or metadata of an asset or the list of assets in a collection. [`PHChange`](../Photos/phchange.md) objects provide information about object state before and after each change with semantics that make it easy to update a collection view or similar interface.

For information about handling changes, see the [`PHPhotoLibraryChangeObserver`](../Photos/phphotolibrarychangeobserver.md) protocol.

## See Also

### Observing Library Changes
- [func register(any PHPhotoLibraryChangeObserver)](../Photos/phphotolibrary/register%28_%29-6y3b9.md)
  Registers an object to receive messages when objects in the photo library change.
- [func unregisterChangeObserver(any PHPhotoLibraryChangeObserver)](../Photos/phphotolibrary/unregisterchangeobserver%28_%29.md)
  Unregisters an object so that it no longer receives change messages.
- [protocol PHPhotoLibraryChangeObserver](../Photos/phphotolibrarychangeobserver.md)
  A protocol to adopt to have the system notify your app of changes to the photo library.
- [class PHChange](../Photos/phchange.md)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](../Photos/phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](../Photos/phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/observing-changes-in-the-photo-library)*