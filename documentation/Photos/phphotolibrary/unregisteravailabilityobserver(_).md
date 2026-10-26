# unregisterAvailabilityObserver(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Unregisters an object from observing changes to the photo library’s availability.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func unregisterAvailabilityObserver(_ observer: any PHPhotoLibraryAvailabilityObserver)
```

```objc
- (void) unregisterAvailabilityObserver:(id<PHPhotoLibraryAvailabilityObserver>) observer;
```

## Parameters

- `observer`: The observer object to unregister.

## See Also

### Observing Library Availability
- [func register(any PHPhotoLibraryAvailabilityObserver)](./register%28_%29-gm0a.md)
  Registers an object to observe changes to the photo library’s availability.
- [protocol PHPhotoLibraryAvailabilityObserver](../phphotolibraryavailabilityobserver.md)
  A protocol to adopt to have the system notify your app when the availability of a photo library changes.
- [var unavailabilityReason: (any Error)?](./unavailabilityreason.md)
  An error that describes the reason the photo library isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/unregisteravailabilityobserver(_:))*