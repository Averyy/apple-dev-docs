# navigationBar

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An action that appears in the navigation bar when the user puts the document browser in Select mode.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var navigationBar: UIDocumentBrowserAction.Availability { get }
```

```c
UIDocumentBrowserActionAvailabilityNavigationBar
```

#### Discussion

The system enables this action as soon as the user makes a valid selection, as determined by the [`supportedContentTypes`](../supportedcontenttypes.md) and [`supportsMultipleItems`](../supportsmultipleitems.md) properties.

> **Note**:  In Mac apps built with Mac Catalyst, the system shows [`navigationBar`](./navigationbar.md) actions as [`menu`](./menu.md) actions.

## See Also

### Constants
- [static var menu: UIDocumentBrowserAction.Availability](./menu.md)
  An action that appears in the Edit Menu when the user long presses a supported document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.struct/navigationbar)*