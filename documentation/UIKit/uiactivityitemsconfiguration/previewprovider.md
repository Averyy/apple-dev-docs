# previewProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A closure that provides previews for the activity items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var previewProvider: ((Int, UIActivityItemsConfigurationPreviewIntent, CGSize) -> NSItemProvider?)? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSItemProvider * (^previewProvider)(NSInteger index, UIActivityItemsConfigurationPreviewIntent intent, CGSize suggestedSize);
```

## See Also

### Managing previews
- [struct UIActivityItemsConfigurationPreviewIntent](../uiactivityitemsconfigurationpreviewintent.md)
  A structure that specifies the types of activity item previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfiguration/previewprovider)*