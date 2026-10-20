# delegate

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the app controller object.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
weak var delegate: (any TVApplicationControllerDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<TVApplicationControllerDelegate> delegate;
```

#### Discussion

The delegate provides methods for observing and managing different `TVApplicationController` object states. [`TVApplicationControllerDelegate`](../tvapplicationcontrollerdelegate.md) provides callbacks during the launch of the JavaScript application.

## See Also

### Getting the Delegate
- [protocol TVApplicationControllerDelegate](../tvapplicationcontrollerdelegate.md)
  A protocol used to observe and manage the different states of an application controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/delegate)*