# init(albumIdentifier:photoLibrary:)

**Framework**: PhotosUI  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(albumIdentifier: String, photoLibrary: PHPhotoLibrary)
```

```objc
- (instancetype) initWithAlbumIdentifier:(NSString *) albumIdentifier photoLibrary:(PHPhotoLibrary *) photoLibrary;
```

#### Discussion

Returns a view controller that allows the user to customize a specified shared album.

Only the system photo library is supported, so `albumIdentifier` must be for an album in the system photo library. If `albumIdentifier` is from a different library, showing a customization sheet will fail.

## Parameters

- `albumIdentifier`: The identifier of the shared album to be customized.
- `photoLibrary`: The photo library in which the specified shared album exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller/init(albumidentifier:photolibrary:))*