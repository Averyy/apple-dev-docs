# photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func photosSharedAlbumPostingSheet(isPresented: Binding<Bool>, items: [PhotosPickerItem], defaultAlbumIdentifier: String? = nil, photoLibrary: PHPhotoLibrary, completion: ((Result<String, any Error>) -> Void)? = nil) -> some View
```

**Other overloads**:

```swift
nonisolated
func photosSharedAlbumPostingSheet(isPresented: Binding<Bool>, items: [PHPickerResult], defaultAlbumIdentifier: String? = nil, photoLibrary: PHPhotoLibrary, completion: ((Result<String, any Error>) -> Void)? = nil) -> some View
```

## Parameters

- `isPresented`: The binding to whether the sheet should be shown.
- `items`: The items to be posted to the shared album.
- `defaultAlbumIdentifier`: Identifier for the shared album to be pre-selected. If none provided user can manually choose the shared album in UI.
- `photoLibrary`: Library to choose from.
- `completion`: Called with the result on completion of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photossharedalbumpostingsheet(ispresented:items:defaultalbumidentifier:photolibrary:completion:)-9fot8)*