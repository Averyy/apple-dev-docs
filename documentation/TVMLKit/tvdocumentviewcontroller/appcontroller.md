# appController

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The document’s app controller that bridges UI, navigation stack, storage, and event handling from JavaScript.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
weak var appController: TVApplicationController? { get }
```

```objc
@property (nonatomic, weak, readonly) TVApplicationController * appController;
```

## See Also

### Accessing the Document’s Components
- [var documentContext: [String : Any]](./documentcontext.md)
  The current document context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/appcontroller)*