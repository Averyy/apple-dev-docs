# navigationBar

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

The system enables this action as soon as the user makes a valid selection, as determined by the [`supportedContentTypes`](uidocumentbrowseraction/supportedcontenttypes.md) and [`supportsMultipleItems`](uidocumentbrowseraction/supportsmultipleitems.md) properties.

> **Note**:  In Mac apps built with Mac Catalyst, the system shows [`navigationBar`](uidocumentbrowseraction/availability-swift.struct/navigationbar.md) actions as [`menu`](uidocumentbrowseraction/availability-swift.struct/menu.md) actions.

## See Also

- [static var menu: UIDocumentBrowserAction.Availability](uidocumentbrowseraction/availability-swift.struct/menu.md)
  An action that appears in the Edit Menu when the user long presses a supported document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.struct/navigationbar)*