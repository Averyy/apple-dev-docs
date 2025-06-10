# postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)

**Framework**: SwiftUI  
**Kind**: method

Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func postToPhotosSharedAlbumSheet(isPresented: Binding<Bool>, items: [PHPickerResult], photoLibrary: PHPhotoLibrary, defaultAlbumIdentifier: String? = nil, completion: ((Result<Void, any Error>) -> Void)? = nil) -> some View
```

#### Discussion

- isPresented: The binding to whether the sheet should be shown.
- items: The items to be posted to the shared album.
- photoLibrary: Library to choose from.
- defaultAlbumIdentifier: Identifier for the shared album to be pre-selected. If none provided user can manually choose the shared album in UI.
- completion: Called with the result on completion of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/posttophotossharedalbumsheet(ispresented:items:photolibrary:defaultalbumidentifier:completion:))*