# photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a view for allowing the user to create a new shared album.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String? = nil, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy? = nil, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)? = nil) -> some View
```

#### Discussion

> **Note**:  When creation is finished, `onCompletion` will be called before`isPresented` is set to `false`. If the user cancels creation, `isPresented` will be set to `false` and `onCompletion` will not be called.

## Parameters

- `isPresented`: The binding for whether the shared album creation view should be shown.
- `defaultTitle`: The default title for the shared album. Useful for suggesting a relevant title to the user.
- `defaultSharingPolicy`: The default sharing policy of the shared album. If `nil`, this defaults to `.private`.
- `photoLibrary`: The photo library in which the shared album will be created.
- `onCompletion`: The callback that will be invoked when shared album creation has succeeded or failed. On success, the result’s `albumIdentifier` and `albumURL` will be non-nil. On failure, the result’s `error` will be non-nil.

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
- [func photosSharedAlbumCustomizationSheet(isPresented: Binding<Bool>, albumIdentifier: String?, photoLibrary: PHPhotoLibrary, onCompletion: (((any Error)?) -> Void)?) -> some View](view/photossharedalbumcustomizationsheet(ispresented:albumidentifier:photolibrary:oncompletion:).md)
  Presents a view for allowing the user to customize a specified shared album.
- [func photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](view/photossharedalbumpostingsheet(ispresented:items:defaultalbumidentifier:photolibrary:completion:).md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photossharedalbumcreationsheet(ispresented:defaulttitle:defaultsharingpolicy:photolibrary:oncompletion:))*