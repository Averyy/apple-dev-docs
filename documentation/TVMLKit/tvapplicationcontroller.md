# TVApplicationController

**Framework**: TVMLKit  
**Kind**: class

An object that bridges the UI, navigation stack, storage, and event handling from JavaScript.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVApplicationController
```

## Mentions

- [Creating TVML Elements](creating-tvml-elements.md)

#### Overview

The `TVApplicationController` class establishes the JavaScript environment and provides a centralized point of control and coordination between the JavaScript environment and tvOS.

## Topics

### Creating a New App Controller
- [init(context: TVApplicationControllerContext, window: UIWindow?, delegate: (any TVApplicationControllerDelegate)?)](tvapplicationcontroller/init(context:window:delegate:).md)
  Initializes and returns an app controller.
### Controlling and Handling Events
- [func evaluate(inJavaScriptContext: (JSContext) -> Void, completion: ((Bool) -> Void)?)](tvapplicationcontroller/evaluate(injavascriptcontext:completion:).md)
  Evaluates a block in the JavaScript execution queue.
- [func stop()](tvapplicationcontroller/stop.md)
  Ends the app life cycle.
### Getting the Delegate
- [var delegate: (any TVApplicationControllerDelegate)?](tvapplicationcontroller/delegate.md)
  The delegate of the app controller object.
- [protocol TVApplicationControllerDelegate](tvapplicationcontrollerdelegate.md)
  A protocol used to observe and manage the different states of an application controller.
### Examining App Controller Properties
- [var context: TVApplicationControllerContext](tvapplicationcontroller/context.md)
  The launch information for the application controller.
- [var navigationController: UINavigationController](tvapplicationcontroller/navigationcontroller.md)
  The navigation controller that is bridged from JavaScript to tvOS.
- [var window: UIWindow?](tvapplicationcontroller/window.md)
  A reference to the window supplied when the app controller was initialized.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Implementing a Hybrid TV App with TVMLKit](implementing-a-hybrid-tv-app-with-tvmlkit.md)
  Display content options with document view controllers and fetch and populate content with TVMLKit JS.
- [class TVApplicationControllerContext](tvapplicationcontrollercontext.md)
  Launch information provided to the TV application controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller)*