# navigationController

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The navigation controller that is bridged from JavaScript to tvOS.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var navigationController: UINavigationController { get }
```

```objc
@property (nonatomic, readonly) UINavigationController * navigationController;
```

#### Discussion

The root controller in which all content is presented. Native controllers can also be pushed onto this controller, or they may be presented manually.

## See Also

### Examining App Controller Properties
- [var context: TVApplicationControllerContext](./context.md)
  The launch information for the application controller.
- [var window: UIWindow?](./window.md)
  A reference to the window supplied when the app controller was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/navigationcontroller)*