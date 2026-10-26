# PhotosPickerItem

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

A type that represents an item you use with a Photos picker.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct PhotosPickerItem
```

#### Overview

The selection results you get from [`PhotosPicker`](./photospicker.md) are placeholder objects. A [`PhotosPickerItem`](./photospickeritem.md) conforms to [`Transferable`](../CoreTransferable/transferable.md), and allows you to load the representation you request. To load a SwiftUI [`Image`](../SwiftUI/image.md) and track progress, use [`loadTransferable(type:completionHandler:)`](./photospickeritem/loadtransferable%28type,completionhandler%29.md).

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

### Creating a picker item
- [init(itemIdentifier: String)](./photospickeritem/init%28itemidentifier%29.md)
  Creates a picker item with the identifier you specify, and without any representation.
### Inspecting a picker item
- [var itemIdentifier: String?](./photospickeritem/itemidentifier.md)
  The local identifier of the item.
- [var supportedContentTypes: [UTType]](./photospickeritem/supportedcontenttypes.md)
  The content types the item supports in order of the most preferred to the least.
### Getting an encoding policy
- [PhotosPickerItem.EncodingDisambiguationPolicy](./photospickeritem/encodingdisambiguationpolicy.md)
  A type that determines the encoding to use when multiple encodings are available, based on the content type.
### Loading the provider’s contents
- [func loadTransferable<T>(type: T.Type) async throws -> sending T?](./photospickeritem/loadtransferable%28type%29.md)
  Attempts to load an instance of the type you specify from the item provider.
- [func loadTransferable<T>(type: T.Type, completionHandler: (Result<T?, any Error>) -> Void) -> Progress](./photospickeritem/loadtransferable%28type,completionhandler%29.md)
  Attempts to load an instance of the type you specify from the item provider, with a completion handler.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Photos picker for SwiftUI
- [Bringing Photos picker to your SwiftUI app](../PhotoKit/bringing-photos-picker-to-your-swiftui-app.md)
  Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](../PhotoKit/implementing-an-inline-photos-picker.md)
  Embed a system-provided, half-height Photos picker into your app’s view.
- [struct PhotosPicker](./photospicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
- [struct PhotosPickerSelectionBehavior](./photospickerselectionbehavior.md)
  A type that describes how the Photos picker handles user selection.
- [struct PhotosPickerStyle](./photospickerstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospickeritem)*