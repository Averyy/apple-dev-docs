# PHPhotoLibraryAvailabilityObserver

**Framework**: Photos  
**Kind**: protocol  
**Role**: Protocol

A protocol to adopt to have the system notify your app when the availability of a photo library changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol PHPhotoLibraryAvailabilityObserver : NSObjectProtocol
```

```objc
@protocol PHPhotoLibraryAvailabilityObserver <NSObject>
```

## Overview

Observing changes to the photo library’s availability is primarily of concern with Mac apps created using macOS and Mac Catalyst, where the library may reside on an external drive or in cloud storage.

## Topics

### Observing Availability Changes
- [func photoLibraryDidBecomeUnavailable(PHPhotoLibrary)](./phphotolibraryavailabilityobserver/photolibrarydidbecomeunavailable%28_%29.md)
  Tells the observer that the photo library’s availability changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Observing Library Availability
- [func register(any PHPhotoLibraryAvailabilityObserver)](./phphotolibrary/register%28_%29-gm0a.md)
  Registers an object to observe changes to the photo library’s availability.
- [func unregisterAvailabilityObserver(any PHPhotoLibraryAvailabilityObserver)](./phphotolibrary/unregisteravailabilityobserver%28_%29.md)
  Unregisters an object from observing changes to the photo library’s availability.
- [var unavailabilityReason: (any Error)?](./phphotolibrary/unavailabilityreason.md)
  An error that describes the reason the photo library isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibraryavailabilityobserver)*