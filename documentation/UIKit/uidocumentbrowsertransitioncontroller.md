# UIDocumentBrowserTransitionController

**Framework**: UIKit  
**Kind**: class

An object that implements the standard loading and transition animations for a document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDocumentBrowserTransitionController
```

#### Overview

Each transition controller is associated with a document in the document browser. The transition controller can provide two separate animation sequences for this document:

- If you set the [`loadingProgress`](uidocumentbrowsertransitioncontroller/loadingprogress.md) property, the document browser shows the loading progress in the document’s thumbnail.
- If you set the [`targetView`](uidocumentbrowsertransitioncontroller/targetview.md) property, the transition controller acts as a [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) object, providing a custom transition between the document’s thumbnail and the target view. This transitioning object can be used both when presenting and when dismissing the document.

You don’t instantiate instances of [`UIDocumentBrowserTransitionController`](uidocumentbrowsertransitioncontroller.md) yourself. Instead, call the document browser’s [`transitionController(forDocumentURL:)`](uidocumentbrowserviewcontroller/transitioncontroller(fordocumenturl:).md) method to get a transition controller for the specified document.

> **Note**:  In Mac apps built with Mac Catalyst, the transition controller doesn’t trigger animations because the macOS design doesn’t use animations for opening or closing documents.

## Topics

### Animating transitions
- [var loadingProgress: Progress?](uidocumentbrowsertransitioncontroller/loadingprogress.md)
  A progress object that tracks a document as it loads.
- [var targetView: UIView?](uidocumentbrowsertransitioncontroller/targetview.md)
  The target view for transition animations when presenting or dismissing the transition controller’s document.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [UIViewControllerAnimatedTransitioning](uiviewcontrolleranimatedtransitioning.md)

## See Also

- [class UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
- [func transitionController(forDocumentAt: URL) -> UIDocumentBrowserTransitionController](uidocumentbrowserviewcontroller/transitioncontroller(fordocumentat:).md)
  Creates a transition controller that provides the standard system-loading and segue animations for the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowsertransitioncontroller)*