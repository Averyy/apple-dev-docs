# register(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Registers an object to observe changes to the photo library’s availability.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func register(_ observer: any PHPhotoLibraryAvailabilityObserver)
```

```objc
- (void) registerAvailabilityObserver:(id<PHPhotoLibraryAvailabilityObserver>) observer;
```

## Parameters

- `observer`: The observer object to register.

## See Also

### Observing Library Availability
- [func unregisterAvailabilityObserver(any PHPhotoLibraryAvailabilityObserver)](./unregisteravailabilityobserver%28_%29.md)
  Unregisters an object from observing changes to the photo library’s availability.
- [protocol PHPhotoLibraryAvailabilityObserver](../phphotolibraryavailabilityobserver.md)
  A protocol to adopt to have the system notify your app when the availability of a photo library changes.
- [var unavailabilityReason: (any Error)?](./unavailabilityreason.md)
  An error that describes the reason the photo library isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-gm0a)*