# context

**Framework**: TVMLKit  
**Kind**: property

The launch information for the application controller.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var context: TVApplicationControllerContext { get }
```

#### Discussion

The launch information contains the JavaScript application URL, [`storageIdentifier`](tvapplicationcontrollercontext/storageidentifier.md), and [`launchOptions`](tvapplicationcontrollercontext/launchoptions.md). The URL can point to a local or remote resource. `launchOptions` can be constructed and forwarded from launch options keys that are part of UIApplication. See Launch Options Keys.

## See Also

- [var navigationController: UINavigationController](tvapplicationcontroller/navigationcontroller.md)
  The navigation controller that is bridged from JavaScript to tvOS.
- [var window: UIWindow?](tvapplicationcontroller/window.md)
  A reference to the window supplied when the app controller was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/context)*