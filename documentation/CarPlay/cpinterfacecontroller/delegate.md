# delegate

**Framework**: CarPlay  
**Kind**: property

An object that serves as the delegate to the interface controller.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any CPInterfaceControllerDelegate)? { get set }
```

## See Also

- [protocol CPInterfaceControllerDelegate](cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](cpinterfacecontroller/prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/setroottemplate(_:animated:completion:).md)
  Sets the root template of the navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/delegate)*