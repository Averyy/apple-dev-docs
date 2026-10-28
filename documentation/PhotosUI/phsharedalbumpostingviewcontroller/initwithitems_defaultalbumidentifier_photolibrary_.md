# initWithItems:defaultAlbumIdentifier:photoLibrary:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (instancetype) initWithItems:(NSArray<PHPickerResult *> *) items defaultAlbumIdentifier:(NSString *) defaultAlbumIdentifier photoLibrary:(PHPhotoLibrary *) photoLibrary;
```

## Discussion

Returns a view controller that allows the user to create a new shared album.

## Parameters

- `items`: The items to be posted to the shared album.
- `defaultAlbumIdentifier`: Identifier for the shared album to be pre-selected. If none provided, the user can manually choose a shared album.
- `photoLibrary`: The photo library to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller/initwithitems:defaultalbumidentifier:photolibrary:)*