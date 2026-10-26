# PhotosPickerSelectionBehavior

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

A type that describes how the Photos picker handles user selection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
struct PhotosPickerSelectionBehavior
```

## Topics

### Getting standard selection behaviors
- [static let `default`: PhotosPickerSelectionBehavior](./photospickerselectionbehavior/default.md)
  Uses the default selection behavior.
- [static let ordered: PhotosPickerSelectionBehavior](./photospickerselectionbehavior/ordered.md)
  Uses the selection order the user made, numbering the selected items.
### Type Properties
- [static let continuous: PhotosPickerSelectionBehavior](./photospickerselectionbehavior/continuous.md)
- [static let continuousAndOrdered: PhotosPickerSelectionBehavior](./photospickerselectionbehavior/continuousandordered.md)

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
- [struct PhotosPickerItem](./photospickeritem.md)
  A type that represents an item you use with a Photos picker.
- [struct PhotosPickerStyle](./photospickerstyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/photospickerselectionbehavior)*