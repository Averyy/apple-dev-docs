# PHChange

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A description of a change that occurred in the photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHChange
```

```objc
@interface PHChange : NSObject
```

## Mentions

- [Observing Changes in the Photo Library](../PhotoKit/observing-changes-in-the-photo-library.md)

#### Overview

Photos provides [`PHChange`](./phchange.md) objects to notify your app of changes to the assets and collections managed by the Photos app. To receive change information, adopt the [`PHPhotoLibraryChangeObserver`](./phphotolibrarychangeobserver.md) protocol and register your observer with the shared [`PHPhotoLibrary`](./phphotolibrary.md) object.

After Photos provides a change object, you use its methods to get a change details object. Call the [`changeDetailsForObject:`](./phchange/changedetailsforobject_.md) or [`changeDetails(for:)`](./phchange/changedetails%28for%29-33a6n.md) method, passing an asset or collection object you’ve previously fetched or a fetch result containing several such objects. The resulting [`PHObjectChangeDetails`](./phobjectchangedetails.md) or [`PHFetchResultChangeDetails`](./phfetchresultchangedetails.md) object describes any changes that have happened to the object or fetch result since you last fetched it.

## Topics

### Getting Change Details
- [func changeDetails(for: PHFetchResult<AnyObject>) -> PHFetchResultChangeDetails<PHObject>?](./phchange/changedetails%28for%29-33a6n.md)
- [func changeDetails<T>(for: T) -> PHObjectChangeDetails<T>?](./phchange/changedetails%28for%29-536rd.md)
  Returns detailed change information for the specified asset or collection.
- [func changeDetails<T>(for: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>?](./phchange/changedetails%28for%29-2fne7.md)
  Returns detailed change information for a fetch result.

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
- [class PHObjectChangeDetails](./phobjectchangedetails.md)
  A description of changes that occurred in an asset or collection object.
- [class PHFetchResultChangeDetails](./phfetchresultchangedetails.md)
  A description of changes that occurred in the set of asset or collection objects listed in a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phchange)*