# init(selection:matching:preferredItemEncoding:label:)

**Framework**: PhotosUI  
**Kind**: init  
**Role**: Initializer

Creates a picker that selects an item and optionally configures the types of items to show, item encoding, and label behavior.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
nonisolated init(selection: Binding<PhotosPickerItem?>, matching filter: PHPickerFilter? = nil, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy = .automatic, @ViewBuilder label: @Sendable () -> Label)
```

## Parameters

- `selection`: The item the picker displays in a selected state.
- `filter`: The types of items that the picker shows.
- `preferredItemEncoding`: The encoding policy of the selection.
- `label`: The view that describes the action of choosing an item.

## See Also

### Creating a picker
- [init(selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, label: () -> Label)](./init%28selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,label%29.md)
  Creates a picker that selects a collection of items and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary, label: () -> Label)](./init%28selection,matching,preferreditemencoding,photolibrary,label%29.md)
  Creates a picker that selects an item from the photo library you specify and optionally configures the types of items to show, item encoding, and label behavior.
- [init(selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary, label: () -> Label)](./init%28selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary,label%29.md)
  Creates a picker that selects a collection of items from the photo library you specify and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospicker/init(selection:matching:preferreditemencoding:label:))*