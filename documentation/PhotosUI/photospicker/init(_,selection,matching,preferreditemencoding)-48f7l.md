# init(_:selection:matching:preferredItemEncoding:)

**Framework**: PhotosUI  
**Kind**: init  
**Role**: Initializer

Creates a picker with a title and selection, and optionally configures the types of items to show and item encoding behavior.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, selection: Binding<PhotosPickerItem?>, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic) where S : StringProtocol
```

Available when `Label` is `Text`.

## Parameters

- `title`: A string that describes the purpose of showing the picker.
- `selection`: The item the picker displays in a selected state.
- `filter`: The types of items that the picker shows.
- `preferredItemEncoding`: The encoding policy of the selection.

## See Also

### Creating a picker with a title
- [init(LocalizedStringKey, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./init%28_,selection,matching,preferreditemencoding%29-7jbef.md)
  Creates a picker with a title key and selection, and optionally configures the types of items to show and item encoding behavior.
- [init(LocalizedStringKey, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding%29-8ac23.md)
  Creates a picker with a title key and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init<S>(S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding%29-6m11r.md)
  Creates a picker with a title and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(LocalizedStringKey, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./init%28_,selection,matching,preferreditemencoding,photolibrary%29-bu7c.md)
  Creates a picker with a title key and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init<S>(S, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./init%28_,selection,matching,preferreditemencoding,photolibrary%29-6bm2n.md)
  Creates a picker with a title and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init(LocalizedStringKey, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary%29-5tpfd.md)
  Creates a picker with a title key and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init<S>(S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary%29-6fwsc.md)
  Creates a picker with a title and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospicker/init(_:selection:matching:preferreditemencoding:)-48f7l)*