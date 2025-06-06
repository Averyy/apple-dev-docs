# prefersDarkUserInterfaceStyle

**Framework**: CarPlay  
**Kind**: property

A Boolean value that determines whether the system draws the user interface in Dark Mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var prefersDarkUserInterfaceStyle: Bool { get set }
```

#### Discussion

To adopt the dark user interface style, set this value to [`true`](https://developer.apple.com/documentation/swift/true) before you provide the root template or push any templates. The default value is [`false`](https://developer.apple.com/documentation/swift/false), which allows templates to change between light and dark styles.

## See Also

- [var delegate: (any CPInterfaceControllerDelegate)?](cpinterfacecontroller/delegate.md)
  An object that serves as the delegate to the interface controller.
- [protocol CPInterfaceControllerDelegate](cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/setroottemplate(_:animated:completion:).md)
  Sets the root template of the navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/prefersdarkuserinterfacestyle)*