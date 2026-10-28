# photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a view for allowing the user to customize a specified shared album.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func photosSharedAlbumCustomizationSheet(isPresented: Binding<Bool>, albumIdentifier: String?, photoLibrary: PHPhotoLibrary, onCompletion: (((any Error)?) -> Void)? = nil) -> some View
```

## Discussion

> **Remark**:  In order for the interface to appear, both `isPresented` must be `true` and `albumIdentifier` must not be `nil`. When the customization is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels customization, `isPresented` will be set to `false` and `onCompletion` will not be called.

## Parameters

- `isPresented`: The binding for whether the shared album customization sheet should be shown.
- `albumIdentifier`: The identifier of the shared album to be customized. Must be non-nil by the time `isPresented` is set to `true`.
- `photoLibrary`: The photo library in which the specified shared album exists.
- `onCompletion`: The callback that will be invoked when the customization has succeeded or failed. On failure, the error will be non-nil.

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
- [func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String?, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy?, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)?) -> some View](./photossharedalbumcreationsheet%28ispresented,defaulttitle,defaultsharingpolicy,photolibrary,oncompletion%29.md)
  Presents a view for allowing the user to create a new shared album.
- [func photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](./photossharedalbumpostingsheet%28ispresented,items,defaultalbumidentifier,photolibrary,completion%29.md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func photosReferenceImageViewer(asset: Binding<PHAsset?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./photosreferenceimageviewer%28asset,onprocessingcompletion%29.md)
  Presents an image viewer for an asset in a photo library that contains Apple Reference Image data when `asset` is set.
- [func photosReferenceImageViewer(fileURL: Binding<URL?>, onProcessingCompletion: ((Result<URL, any Error>) -> Void)?) -> some View](./photosreferenceimageviewer%28fileurl,onprocessingcompletion%29.md)
  Presents an image viewer for a given image file containing Apple Reference Image data when `fileURL` is set.
- [func photosReferenceImageViewer(pickerItem: Binding<PhotosPickerItem?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./photosreferenceimageviewer%28pickeritem,onprocessingcompletion%29.md)
  Presents an image viewer for an image containing Apple Reference Image data selected from the Photos picker when `pickerItem` is set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photossharedalbumcustomizationsheet(ispresented:albumidentifier:photolibrary:oncompletion:))*