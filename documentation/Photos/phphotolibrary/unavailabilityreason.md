# unavailabilityReason

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An error that describes the reason the photo library isn’t available.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var unavailabilityReason: (any Error)? { get }
```

```objc
@property (atomic, strong, readonly, nullable) NSError * unavailabilityReason;
```

#### Discussion

This property contains a valid error only when the library is unavailable.

## See Also

### Observing Library Availability
- [func register(any PHPhotoLibraryAvailabilityObserver)](./register%28_%29-gm0a.md)
  Registers an object to observe changes to the photo library’s availability.
- [func unregisterAvailabilityObserver(any PHPhotoLibraryAvailabilityObserver)](./unregisteravailabilityobserver%28_%29.md)
  Unregisters an object from observing changes to the photo library’s availability.
- [protocol PHPhotoLibraryAvailabilityObserver](../phphotolibraryavailabilityobserver.md)
  A protocol to adopt to have the system notify your app when the availability of a photo library changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/unavailabilityreason)*