# photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a view for allowing the user to create a new shared album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String? = nil, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy? = nil, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)? = nil) -> some View
```

## Discussion

> **Remark**:  When creation is finished, `onCompletion` will be called before`isPresented` is set to `false`. If the user cancels creation, `isPresented` will be set to `false` and `onCompletion` will not be called.

## Parameters

- `isPresented`: The binding for whether the shared album creation view should be shown.
- `defaultTitle`: The default title for the shared album. Useful for suggesting a relevant title to the user.
- `defaultSharingPolicy`: The default sharing policy of the shared album. If `nil`, this defaults to `.private`.
- `photoLibrary`: The photo library in which the shared album will be created.
- `onCompletion`: The callback that will be invoked when shared album creation has succeeded or failed. On success, the result’s `albumIdentifier` and `albumURL` will be non-nil. On failure, the result’s `error` will be non-nil.

## See Also

### Selecting photos
- [struct PhotosPicker](../../PhotosUI/photospicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](./photospicker%28ispresented,selection,matching,preferreditemencoding%29.md)
  Presents a Photos picker that selects a `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](./photospicker%28ispresented,selection,matching,preferreditemencoding,photolibrary%29.md)
  Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](./photospicker%28ispresented,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding%29.md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](./photospicker%28ispresented,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary%29.md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some View](./photospickeraccessoryvisibility%28_,edges%29.md)
  Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View](./photospickerdisabledcapabilities%28_%29.md)
  Disables capabilities of the Photos picker.
- [func photosPickerSearchText(_:)](./photospickersearchtext%28_%29.md)
  Sets search text of the Photos picker.
- [func photosPickerStyle(PhotosPickerStyle) -> some View](./photospickerstyle%28_%29.md)
  Sets the mode of the Photos picker.
- [func photosPickerMetadataOptions(PHPickerMetadataOptions) -> some View](./photospickermetadataoptions%28_%29.md)
  Sets metadata options for the Photos picker.
- [func photosSharedAlbumCustomizationSheet(isPresented: Binding<Bool>, albumIdentifier: String?, photoLibrary: PHPhotoLibrary, onCompletion: (((any Error)?) -> Void)?) -> some View](./photossharedalbumcustomizationsheet%28ispresented,albumidentifier,photolibrary,oncompletion%29.md)
  Presents a view for allowing the user to customize a specified shared album.
- [func photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](./photossharedalbumpostingsheet%28ispresented,items,defaultalbumidentifier,photolibrary,completion%29.md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func photosReferenceImageViewer(asset: Binding<PHAsset?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./photosreferenceimageviewer%28asset,onprocessingcompletion%29.md)
  Presents an image viewer for an asset in a photo library that contains Apple Reference Image data when `asset` is set.
- [func photosReferenceImageViewer(fileURL: Binding<URL?>, onProcessingCompletion: ((Result<URL, any Error>) -> Void)?) -> some View](./photosreferenceimageviewer%28fileurl,onprocessingcompletion%29.md)
  Presents an image viewer for a given image file containing Apple Reference Image data when `fileURL` is set.
- [func photosReferenceImageViewer(pickerItem: Binding<PhotosPickerItem?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./photosreferenceimageviewer%28pickeritem,onprocessingcompletion%29.md)
  Presents an image viewer for an image containing Apple Reference Image data selected from the Photos picker when `pickerItem` is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photossharedalbumcreationsheet(ispresented:defaulttitle:defaultsharingpolicy:photolibrary:oncompletion:))*