# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An object that serves as the delegate to the interface controller.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: (any CPInterfaceControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<CPInterfaceControllerDelegate> delegate;
```

## See Also

### Configuring the Interface Controller
- [protocol CPInterfaceControllerDelegate](../cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](./prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./setroottemplate%28_,animated,completion%29.md)
  Sets the root template of the navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/delegate)*