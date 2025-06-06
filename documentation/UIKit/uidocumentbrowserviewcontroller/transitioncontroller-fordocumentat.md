# transitionController(forDocumentAt:)

**Framework**: Uikit  
**Kind**: method

Creates a transition controller that provides the standard system-loading and segue animations for the document browser.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func transitionController(forDocumentAt documentURL: URL) -> UIDocumentBrowserTransitionController
```

#### Return Value

Returns a newly instantiated transition controller. Its [`loadingProgress`](uidocumentbrowsertransitioncontroller/loadingprogress.md) and [`targetView`](uidocumentbrowsertransitioncontroller/targetview.md) properties are both set to `nil`.

#### Discussion

For the animations to function properly, you must maintain a strong reference to the transition controller until all the animation sequences are complete.

For more about using the transition controller, see [`UIDocumentBrowserTransitionController`](uidocumentbrowsertransitioncontroller.md).

> **Note**:  In Mac apps built with Mac Catalyst, the transition controller doesn’t generate animations. macOS doesn’t use animations when opening or closing documents.

## Parameters

- `documentURL`: The URL of a document. Only use URLs provided by the document browser (for example, URLs passed to the delegate’s  method’s completion block).

## See Also

- [class UIDocumentBrowserTransitionController](uidocumentbrowsertransitioncontroller.md)
  An object that implements the standard loading and transition animations for a document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/transitioncontroller(fordocumentat:))*