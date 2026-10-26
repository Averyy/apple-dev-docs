# init(items:defaultAlbumIdentifier:photoLibrary:)

**Framework**: PhotosUI  
**Kind**: init  
**Role**: Initializer

Returns a view controller that allows the user to create a new shared album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(items: [PHPickerResult], defaultAlbumIdentifier: String?, photoLibrary: PHPhotoLibrary)
```

## Parameters

- `items`: The items to be posted to the shared album.
- `defaultAlbumIdentifier`: Identifier for the shared album to be pre-selected. If none provided, the user can manually choose a shared album.
- `photoLibrary`: The photo library to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller/init(items:defaultalbumidentifier:photolibrary:))*