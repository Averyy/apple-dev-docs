# dismissPreview(animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the currently active document preview.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func dismissPreview(animated: Bool)
```

```objc
- (void) dismissPreviewAnimated:(BOOL) animated;
```

#### Discussion

Use this method to dismiss the document preview programmatically. The document interaction controller may also dismiss the document preview automatically in response to user actions.

## Parameters

- `animated`: Specify [`true`](../../Swift/true.md) to animate the dismissal of the document preview or [`false`](../../Swift/false.md) to dismiss it immediately.

## See Also

### Presenting and dismissing a document preview
- [func presentPreview(animated: Bool) -> Bool](./presentpreview%28animated%29.md)
  Displays a full-screen preview of the target document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/dismisspreview(animated:))*