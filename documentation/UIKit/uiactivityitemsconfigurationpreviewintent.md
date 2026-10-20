# UIActivityItemsConfigurationPreviewIntent

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A structure that specifies the types of activity item previews.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct UIActivityItemsConfigurationPreviewIntent
```

```c
typedef NSString * UIActivityItemsConfigurationPreviewIntent;
```

## Topics

### Constants
- [static let fullSize: UIActivityItemsConfigurationPreviewIntent](./uiactivityitemsconfigurationpreviewintent/fullsize.md)
  A full-size preview image.
- [static let thumbnail: UIActivityItemsConfigurationPreviewIntent](./uiactivityitemsconfigurationpreviewintent/thumbnail.md)
  A thumbnail preview image.
### Initializers
- [init(String)](./uiactivityitemsconfigurationpreviewintent/init%28_%29.md)
  Creates a preview intent.
- [init(rawValue: String)](./uiactivityitemsconfigurationpreviewintent/init%28rawvalue%29.md)
  Creates a preview intent with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing previews
- [var previewProvider: ((Int, UIActivityItemsConfigurationPreviewIntent, CGSize) -> NSItemProvider?)?](./uiactivityitemsconfiguration/previewprovider.md)
  A closure that provides previews for the activity items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationpreviewintent)*