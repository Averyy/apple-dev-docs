# delegate

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The delegate for handling events in the document view controller.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
weak var delegate: (any TVDocumentViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<TVDocumentViewControllerDelegate> delegate;
```

## See Also

### Managing Interactions with the Document
- [protocol TVDocumentViewControllerDelegate](../tvdocumentviewcontrollerdelegate.md)
  Methods to manage updates, events, and errors from the document view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/delegate)*