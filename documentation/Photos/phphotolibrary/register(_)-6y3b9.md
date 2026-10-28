# register(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Registers an object to receive messages when objects in the photo library change.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func register(_ observer: any PHPhotoLibraryChangeObserver)
```

```objc
- (void) registerChangeObserver:(id<PHPhotoLibraryChangeObserver>) observer;
```

## Mentions

- [Observing Changes in the Photo Library](../../PhotoKit/observing-changes-in-the-photo-library.md)

## Discussion

You implicitly declare interest in change messages whenever you use a fetch method (such as [`fetchAssets(with:)`](../phasset/fetchassets%28with%29.md)) to retrieve assets or collections. After you perform a fetch, Photos automatically sends change messages whenever the objects in the resulting fetch request change—including when changes happen that add to, remove from, or reorder the list of objects in the fetch result.

## Parameters

- `observer`: An object for receiving change messages.

## See Also

### Observing Library Changes
- [Observing Changes in the Photo Library](../../PhotoKit/observing-changes-in-the-photo-library.md)
  Register an observer to be notified of changes to the photo library.
- [func unregisterChangeObserver(any PHPhotoLibraryChangeObserver)](./unregisterchangeobserver%28_%29.md)
  Unregisters an object so that it no longer receives change messages.
- [protocol PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md)
  A protocol to adopt to have the system notify your app of changes to the photo library.
- [class PHChange](../phchange.md)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](../phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](../phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-6y3b9)*