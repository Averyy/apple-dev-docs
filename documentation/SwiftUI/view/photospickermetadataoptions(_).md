# photosPickerMetadataOptions(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets metadata options for the Photos picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func photosPickerMetadataOptions(_ metadataOptions: PHPickerMetadataOptions) -> some View
```

#### Return Value

A Photos picker with specified metadata options.

## Parameters

- `metadataOptions`: One or more of the available metadata options.

## See Also

### Selecting photos
- [struct PhotosPicker](https://developer.apple.com/documentation/photosui/photospicker)
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
- [func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String?, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy?, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)?) -> some View](./photossharedalbumcreationsheet%28ispresented,defaulttitle,defaultsharingpolicy,photolibrary,oncompletion%29.md)
  Presents a view for allowing the user to create a new shared album.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photospickermetadataoptions(_:))*