# activityItemsConfigurationPreviewForItem(at:intent:suggestedSize:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns an activity items configuration preview for the specified item and preview size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func activityItemsConfigurationPreviewForItem(at index: Int, intent: UIActivityItemsConfigurationPreviewIntent, suggestedSize: CGSize) -> NSItemProvider?
```

```objc
- (NSItemProvider *) activityItemsConfigurationPreviewForItemAtIndex:(NSInteger) index intent:(UIActivityItemsConfigurationPreviewIntent) intent suggestedSize:(CGSize) suggestedSize;
```

## See Also

### Managing Previews
- [struct UIActivityItemsConfigurationPreviewIntent](../uiactivityitemsconfigurationpreviewintent.md)
  A structure that specifies the types of activity item previews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationreading/activityitemsconfigurationpreviewforitem(at:intent:suggestedsize:))*