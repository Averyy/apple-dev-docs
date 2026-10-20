# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The document menu’s delegate.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIDocumentMenuViewController`](../uidocumentmenuviewcontroller.md).

## Declaration

```swift
weak var delegate: (any UIDocumentMenuDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIDocumentMenuDelegate> delegate;
```

#### Discussion

The delegate must adopt the [`UIDocumentMenuDelegate`](../uidocumentmenudelegate.md) protocol.

## See Also

### Getting the user-selected document picker
- [protocol UIDocumentMenuDelegate](../uidocumentmenudelegate.md)
  A set of methods that you must implement to track user interactions with a document menu view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/delegate)*