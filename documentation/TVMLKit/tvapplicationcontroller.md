# TVApplicationController

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

An object that bridges the UI, navigation stack, storage, and event handling from JavaScript.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVApplicationController
```

```objc
@interface TVApplicationController : NSObject
```

## Mentions

- [Creating TVML Elements](./creating-tvml-elements.md)

## Overview

The `TVApplicationController` class establishes the JavaScript environment and provides a centralized point of control and coordination between the JavaScript environment and tvOS.

## Topics

### Creating a New App Controller
- [init(context: TVApplicationControllerContext, window: UIWindow?, delegate: (any TVApplicationControllerDelegate)?)](./tvapplicationcontroller/init%28context,window,delegate%29.md)
  Initializes and returns an app controller.
### Controlling and Handling Events
- [func evaluate(inJavaScriptContext: (JSContext) -> Void, completion: ((Bool) -> Void)?)](./tvapplicationcontroller/evaluate%28injavascriptcontext,completion%29.md)
  Evaluates a block in the JavaScript execution queue.
- [func stop()](./tvapplicationcontroller/stop%28%29.md)
  Ends the app life cycle.
### Getting the Delegate
- [var delegate: (any TVApplicationControllerDelegate)?](./tvapplicationcontroller/delegate.md)
  The delegate of the app controller object.
- [protocol TVApplicationControllerDelegate](./tvapplicationcontrollerdelegate.md)
  A protocol used to observe and manage the different states of an application controller.
### Examining App Controller Properties
- [var context: TVApplicationControllerContext](./tvapplicationcontroller/context.md)
  The launch information for the application controller.
- [var navigationController: UINavigationController](./tvapplicationcontroller/navigationcontroller.md)
  The navigation controller that is bridged from JavaScript to tvOS.
- [var window: UIWindow?](./tvapplicationcontroller/window.md)
  A reference to the window supplied when the app controller was initialized.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### JavaScript Environment
- [Implementing a Hybrid TV App with TVMLKit](./implementing-a-hybrid-tv-app-with-tvmlkit.md)
  Display content options with document view controllers and fetch and populate content with TVMLKit JS.
- [class TVApplicationControllerContext](./tvapplicationcontrollercontext.md)
  Launch information provided to the TV application controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller)*