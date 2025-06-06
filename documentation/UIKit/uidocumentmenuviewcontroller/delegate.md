# delegate

**Framework**: UIKit  
**Kind**: property

The document menu’s delegate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any UIDocumentMenuDelegate)? { get set }
```

#### Discussion

The delegate must adopt the [`UIDocumentMenuDelegate`](uidocumentmenudelegate.md) protocol.

## See Also

- [protocol UIDocumentMenuDelegate](uidocumentmenudelegate.md)
  A set of methods that you must implement to track user interactions with a document menu view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/delegate)*