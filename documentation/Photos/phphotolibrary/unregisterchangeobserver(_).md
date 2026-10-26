# unregisterChangeObserver(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Unregisters an object so that it no longer receives change messages.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func unregisterChangeObserver(_ observer: any PHPhotoLibraryChangeObserver)
```

```objc
- (void) unregisterChangeObserver:(id<PHPhotoLibraryChangeObserver>) observer;
```

## Parameters

- `observer`: An object currently registered to receive change messages.

## See Also

### Observing Library Changes
- [Observing Changes in the Photo Library](../../PhotoKit/observing-changes-in-the-photo-library.md)
  Register an observer to be notified of changes to the photo library.
- [func register(any PHPhotoLibraryChangeObserver)](./register%28_%29-6y3b9.md)
  Registers an object to receive messages when objects in the photo library change.
- [protocol PHPhotoLibraryChangeObserver](../phphotolibrarychangeobserver.md)
  A protocol to adopt to have the system notify your app of changes to the photo library.
- [class PHChange](../phchange.md)
  A description of a change that occurred in the photo library.
- [class PHObjectChangeDetails](../phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](../phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/unregisterchangeobserver(_:))*