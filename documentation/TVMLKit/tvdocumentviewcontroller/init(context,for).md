# init(context:for:)

**Framework**: TVMLKit  
**Kind**: init  
**Role**: Initializer

Creates a new document view controller with a specific context and app controller.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
convenience init(context: [String : Any], for appController: TVApplicationController)
```

```objc
+ (instancetype) viewControllerWithContext:(NSDictionary<NSString *,id> *) context forAppController:(TVApplicationController *) appController;
```

#### Discussion

The `context` parameter provides information to `TVMLKit JS` to determine which document to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/init(context:for:))*