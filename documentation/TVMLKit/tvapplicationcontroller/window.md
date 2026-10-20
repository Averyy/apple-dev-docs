# window

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A reference to the window supplied when the app controller was initialized.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var window: UIWindow? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIWindow * window;
```

## See Also

### Examining App Controller Properties
- [var context: TVApplicationControllerContext](./context.md)
  The launch information for the application controller.
- [var navigationController: UINavigationController](./navigationcontroller.md)
  The navigation controller that is bridged from JavaScript to tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/window)*