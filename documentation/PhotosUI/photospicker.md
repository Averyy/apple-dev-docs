# PhotosPicker

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

A view that displays a Photos picker for choosing assets from the photo library.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PhotosPicker<Label> where Label : View
```

## Overview

Use the Photos picker view to browse and select images and videos from the photo library. The view contains methods for single selection and multiple selection. For example, the following code displays a button that — when pressed — shows a picker in multiple selection mode.

```swift
import SwiftUI
import PhotosUI

struct PhotosSelector: View {
    @State var selectedItems: [PhotosPickerItem] = []

    var body: some View {
        PhotosPicker(selection: $selectedItems,
                     matching: .images) {
            Text("Select Multiple Photos")
        }
    }
}
```

When displaying the picker, you can use [`PHPickerFilter`](./phpickerfilter-swift.struct.md) options to customize what it displays. For example, the following code displays [`images`](./phpickerfilter-swift.struct/images.md) and excludes [`screenshots`](./phpickerfilter-swift.struct/screenshots.md).

```swift
PhotosPicker(selection: $selectedItems,
             matching: .any(of: [.images, .not(.screenshots)])) {
    Text("Select Photos")
}
```

The selection results you get are placeholder objects. A [`PhotosPickerItem`](./photospickeritem.md) conforms to [`Transferable`](../CoreTransferable/transferable.md), and allows you to load a representation you request. To load a SwiftUI [`Image`](../SwiftUI/image.md) and track progress, use [`loadTransferable(type:completionHandler:)`](./photospickeritem/loadtransferable%28type,completionhandler%29.md).

```swift
func loadTransferable(from imageSelection: PhotosPickerItem) -> Progress {
    return imageSelection.loadTransferable(type: Image.self) { result in
        DispatchQueue.main.async {
            guard imageSelection == self.imageSelection else { return }
            switch result {
            case .success(let image?):
                // Handle the success case with the image.
            case .success(nil):
                // Handle the success case with an empty value.
            case .failure(let error):
                // Handle the failure case with the provided error.
            }
        }
    }
}
```

A failure can occur when the system attempts to retrieve the data. For example, if the picker tries to download data from iCloud Photos without a network connection.

> ❗ **Important**:  [`Image`](../SwiftUI/image.md) supports only PNG and JPEG file types through its [`Transferable`](../CoreTransferable/transferable.md) conformance. To support other image types, create a custom `Transferable` model. For more information, see [Bringing Photos picker to your SwiftUI app](../PhotoKit/bringing-photos-picker-to-your-swiftui-app.md).

## Topics

### Creating a picker
- [init(selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, label: () -> Label)](./photospicker/init%28selection,matching,preferreditemencoding,label%29.md)
  Creates a picker that selects an item and optionally configures the types of items to show, item encoding, and label behavior.
- [init(selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, label: () -> Label)](./photospicker/init%28selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,label%29.md)
  Creates a picker that selects a collection of items and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary, label: () -> Label)](./photospicker/init%28selection,matching,preferreditemencoding,photolibrary,label%29.md)
  Creates a picker that selects an item from the photo library you specify and optionally configures the types of items to show, item encoding, and label behavior.
- [init(selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary, label: () -> Label)](./photospicker/init%28selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary,label%29.md)
  Creates a picker that selects a collection of items from the photo library you specify and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
### Creating a picker with a title
- [init(LocalizedStringKey, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./photospicker/init%28_,selection,matching,preferreditemencoding%29-7jbef.md)
  Creates a picker with a title key and selection, and optionally configures the types of items to show and item encoding behavior.
- [init<S>(S, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./photospicker/init%28_,selection,matching,preferreditemencoding%29-48f7l.md)
  Creates a picker with a title and selection, and optionally configures the types of items to show and item encoding behavior.
- [init(LocalizedStringKey, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./photospicker/init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding%29-8ac23.md)
  Creates a picker with a title key and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init<S>(S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy)](./photospicker/init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding%29-6m11r.md)
  Creates a picker with a title and selection, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init(LocalizedStringKey, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./photospicker/init%28_,selection,matching,preferreditemencoding,photolibrary%29-bu7c.md)
  Creates a picker with a title key and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init<S>(S, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./photospicker/init%28_,selection,matching,preferreditemencoding,photolibrary%29-6bm2n.md)
  Creates a picker with a title and selection from the photo library you specify, and optionally configures the types of items to show, item encoding, and label behavior.
- [init(LocalizedStringKey, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./photospicker/init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary%29-5tpfd.md)
  Creates a picker with a title key and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.
- [init<S>(S, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary)](./photospicker/init%28_,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary%29-6fwsc.md)
  Creates a picker with a title and selection from the photo library you specify, and optionally configures the max selection count, selection behavior, types of items to show, item encoding, and label behavior.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Photos picker for SwiftUI
- [Bringing Photos picker to your SwiftUI app](../PhotoKit/bringing-photos-picker-to-your-swiftui-app.md)
  Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](../PhotoKit/implementing-an-inline-photos-picker.md)
  Embed a system-provided, half-height Photos picker into your app’s view.
- [struct PhotosPickerItem](./photospickeritem.md)
  A type that represents an item you use with a Photos picker.
- [struct PhotosPickerSelectionBehavior](./photospickerselectionbehavior.md)
  A type that describes how the Photos picker handles user selection.
- [struct PhotosPickerStyle](./photospickerstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospicker)*