# previewProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A visual preview of the drag item, displayed while the user drags the item across the screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var previewProvider: (() -> UIDragPreview?)? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIDragPreview * (^previewProvider)();
```

#### Discussion

As the user drags an item across the screen, the system displays a preview. You can change the preview by setting [`previewProvider`](./previewprovider.md) to a block that returns a [`UIDragPreview`](../uidragpreview.md) object. The system invokes the block if and when it needs the drag item preview.

To use the default preview, set [`previewProvider`](./previewprovider.md) to `nil`. To hide the preview, set [`previewProvider`](./previewprovider.md) to a block that returns `nil`.

## See Also

### Changing the drag item preview
- [func setNeedsDropPreviewUpdate()](./setneedsdroppreviewupdate%28%29.md)
  Notifies the operating system that an updated drop preview is available for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem/previewprovider)*