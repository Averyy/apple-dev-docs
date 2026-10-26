# photoLibraryDidBecomeUnavailable(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that the photo library’s availability changed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func photoLibraryDidBecomeUnavailable(_ photoLibrary: PHPhotoLibrary)
```

```objc
- (void) photoLibraryDidBecomeUnavailable:(PHPhotoLibrary *) photoLibrary;
```

## Parameters

- `photoLibrary`: The photo library whose availability changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibraryavailabilityobserver/photolibrarydidbecomeunavailable(_:))*