# photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)

**Framework**: SwiftUI  
**Kind**: method

Presents a Photos picker that selects a collection of `PhotosPickerItem`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int? = nil, selectionBehavior: PhotosPickerSelectionBehavior = .default, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic) -> some View
```

#### Discussion

The user explicitly grants access only to items they choose, so photo library access authorization is not needed.

## Parameters

- `isPresented`: The binding to whether the Photos picker should be shown.
- `selection`: All items being shown and selected in the Photos picker.
- `maxSelectionCount`: The maximum number of items that can be selected. Default is `nil`. Setting it to `nil` means maximum supported by the system.
- `selectionBehavior`: The selection behavior of the Photos picker. Default is `.default`.
- `filter`: Types of items that can be shown. Default is `nil`. Setting it to `nil` means all supported types can be shown.
- `preferredItemEncoding`: The encoding disambiguation policy of selected items. Default is `.automatic`. Setting it to `.automatic` means the best encoding determined by the system will be used.

## See Also

- [struct PhotosPicker](../PhotosUI/PhotosPicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](view/photospicker(ispresented:selection:matching:preferreditemencoding:).md)
  Presents a Photos picker that selects a `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](view/photospicker(ispresented:selection:matching:preferreditemencoding:photolibrary:).md)
  Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
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
- [func photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](view/photossharedalbumpostingsheet(ispresented:items:defaultalbumidentifier:photolibrary:completion:).md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:))*