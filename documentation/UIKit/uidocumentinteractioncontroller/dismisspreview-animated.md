# dismissPreview(animated:)

**Framework**: UIKit  
**Kind**: method

Dismisses the currently active document preview.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func dismissPreview(animated: Bool)
```

#### Discussion

Use this method to dismiss the document preview programmatically. The document interaction controller may also dismiss the document preview automatically in response to user actions.

## Parameters

- `animated`: Specify   to animate the dismissal of the document preview or   to dismiss it immediately.

## See Also

- [func presentPreview(animated: Bool) -> Bool](uidocumentinteractioncontroller/presentpreview(animated:).md)
  Displays a full-screen preview of the target document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/dismisspreview(animated:))*