# photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)

**Framework**: SwiftUI  
**Kind**: method

Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

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

## See Also

- [struct PhotosPicker](../photosui/photospicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](view/photospicker(ispresented:selection:matching:preferreditemencoding:).md)
  Presents a Photos picker that selects a `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](view/photospicker(ispresented:selection:matching:preferreditemencoding:photolibrary:).md)
  Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:).md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:photolibrary:).md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some View](view/photospickeraccessoryvisibility(_:edges:).md)
  Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View](view/photospickerdisabledcapabilities(_:).md)
  Disables capabilities of the Photos picker.
- [func photosPickerSearchText(_:)](view/photospickersearchtext(_:).md)
  Sets search text of the Photos picker.
- [func photosPickerStyle(PhotosPickerStyle) -> some View](view/photospickerstyle(_:).md)
  Sets the mode of the Photos picker.
- [func photosPickerMetadataOptions(PHPickerMetadataOptions) -> some View](view/photospickermetadataoptions(_:).md)
  Sets metadata options for the Photos picker.
- [func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String?, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy?, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)?) -> some View](view/photossharedalbumcreationsheet(ispresented:defaulttitle:defaultsharingpolicy:photolibrary:oncompletion:).md)
  Presents a view for allowing the user to create a new shared album.
- [func photosSharedAlbumCustomizationSheet(isPresented: Binding<Bool>, albumIdentifier: String?, photoLibrary: PHPhotoLibrary, onCompletion: (((any Error)?) -> Void)?) -> some View](view/photossharedalbumcustomizationsheet(ispresented:albumidentifier:photolibrary:oncompletion:).md)
  Presents a view for allowing the user to customize a specified shared album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photossharedalbumpostingsheet(ispresented:items:defaultalbumidentifier:photolibrary:completion:))*