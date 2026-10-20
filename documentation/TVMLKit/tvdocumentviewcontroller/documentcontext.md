# documentContext

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The current document context.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var documentContext: [String : Any] { get }
```

```objc
@property (nonatomic, strong, readonly) NSDictionary<NSString *,id> * documentContext;
```

#### Discussion

Use this property to retrieve the current context, whether it’s new or updated.

## See Also

### Accessing the Document’s Components
- [var appController: TVApplicationController?](./appcontroller.md)
  The document’s app controller that bridges UI, navigation stack, storage, and event handling from JavaScript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/documentcontext)*