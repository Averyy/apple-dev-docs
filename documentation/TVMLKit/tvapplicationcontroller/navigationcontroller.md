# navigationController

**Framework**: TVMLKit  
**Kind**: property

The navigation controller that is bridged from JavaScript to tvOS.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var navigationController: UINavigationController { get }
```

#### Discussion

The root controller in which all content is presented. Native controllers can also be pushed onto this controller, or they may be presented manually.

## See Also

- [var context: TVApplicationControllerContext](tvapplicationcontroller/context.md)
  The launch information for the application controller.
- [var window: UIWindow?](tvapplicationcontroller/window.md)
  A reference to the window supplied when the app controller was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/navigationcontroller)*