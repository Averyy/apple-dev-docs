# previewProvider

**Framework**: UIKit  
**Kind**: property

A closure that provides previews for the activity items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var previewProvider: ((Int, UIActivityItemsConfigurationPreviewIntent, CGSize) -> NSItemProvider?)? { get set }
```

## See Also

- [struct UIActivityItemsConfigurationPreviewIntent](uiactivityitemsconfigurationpreviewintent.md)
  A structure that specifies the types of activity item previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/previewprovider)*