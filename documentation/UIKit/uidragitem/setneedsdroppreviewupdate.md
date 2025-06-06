# setNeedsDropPreviewUpdate()

**Framework**: UIKit  
**Kind**: method

Notifies the operating system that an updated drop preview is available for the item.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
func setNeedsDropPreviewUpdate()
```

#### Discussion

Call this method to provide an updated drop preview after UIKit has started the drop animation. If the drop animation is still ongoing, UIKit calls the drop interaction delegate’s [`dropInteraction(_:previewForDropping:withDefault:)`](uidropinteractiondelegate/dropinteraction(_:previewfordropping:withdefault:).md) method, passing the previous drop preview as the `defaultPreview`.

## See Also

- [var previewProvider: (() -> UIDragPreview?)?](uidragitem/previewprovider.md)
  A visual preview of the drag item, displayed while the user drags the item across the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem/setneedsdroppreviewupdate())*