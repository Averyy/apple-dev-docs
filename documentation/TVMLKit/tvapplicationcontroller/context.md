# context

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The launch information for the application controller.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var context: TVApplicationControllerContext { get }
```

```objc
@property (nonatomic, readonly) TVApplicationControllerContext * context;
```

## Discussion

The launch information contains the JavaScript application URL, [`storageIdentifier`](../tvapplicationcontrollercontext/storageidentifier.md), and [`launchOptions`](../tvapplicationcontrollercontext/launchoptions.md). The URL can point to a local or remote resource. `launchOptions` can be constructed and forwarded from launch options keys that are part of UIApplication. See Launch Options Keys.

## See Also

### Examining App Controller Properties
- [var navigationController: UINavigationController](./navigationcontroller.md)
  The navigation controller that is bridged from JavaScript to tvOS.
- [var window: UIWindow?](./window.md)
  A reference to the window supplied when the app controller was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/context)*