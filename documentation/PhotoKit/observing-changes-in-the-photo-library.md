# Observing Changes in the Photo Library

**Framework**: PhotoKit  
**Role**: Article

Register an observer to be notified of changes to the photo library.

#### Overview

To be notified of changes to the photo library, use the [`register(_:)`](https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-6y3b9) method to designate an observer object. Whenever you use a fetch method, such as [`fetchAssets(with:)`](https://developer.apple.com/documentation/photos/phasset/fetchassets(with:)), to retrieve assets or collections, Photos automatically registers your interest in observing changes to those items. After you perform a fetch, Photos sends messages to your observer through the [`PHPhotoLibraryChangeObserver`](https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver) protocol whenever the items in the resulting fetch request change. For example, you’ll get notified when changes add items, remove items, or reorder the list of items in the fetch result. Update your user interface based on the details you receive from [`PHChange`](https://developer.apple.com/documentation/photos/phchange) objects.

Use the shared [`PHPhotoLibrary`](https://developer.apple.com/documentation/photos/phphotolibrary) object to register a change handler for the assets and collections you fetch. Photos tells your app whenever another app or device changes the content or metadata of an asset or the list of assets in a collection. [`PHChange`](https://developer.apple.com/documentation/photos/phchange) objects provide information about object state before and after each change with semantics that make it easy to update a collection view or similar interface.

For information about handling changes, see the [`PHPhotoLibraryChangeObserver`](https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver) protocol.

## See Also

### Observing Library Changes
- [func register(any PHPhotoLibraryChangeObserver)](https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-6y3b9)
  Registers an object to receive messages when objects in the photo library change.
- [func unregisterChangeObserver(any PHPhotoLibraryChangeObserver)](https://developer.apple.com/documentation/photos/phphotolibrary/unregisterchangeobserver(_:))
  Unregisters an object so that it no longer receives change messages.
- [protocol PHPhotoLibraryChangeObserver](https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver)
  A protocol to adopt to have the system notify your app of changes to the photo library.
- [class PHChange](https://developer.apple.com/documentation/photos/phchange)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](https://developer.apple.com/documentation/photos/phobjectchangedetails)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](https://developer.apple.com/documentation/photos/phfetchresultchangedetails)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/observing-changes-in-the-photo-library)*