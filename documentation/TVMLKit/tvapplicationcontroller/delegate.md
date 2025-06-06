# delegate

**Framework**: TVMLKit  
**Kind**: property

The delegate of the app controller object.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
weak var delegate: (any TVApplicationControllerDelegate)? { get }
```

#### Discussion

The delegate provides methods for observing and managing different `TVApplicationController` object states. [`TVApplicationControllerDelegate`](tvapplicationcontrollerdelegate.md) provides callbacks during the launch of the JavaScript application.

## See Also

- [protocol TVApplicationControllerDelegate](tvapplicationcontrollerdelegate.md)
  A protocol used to observe and manage the different states of an application controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller/delegate)*