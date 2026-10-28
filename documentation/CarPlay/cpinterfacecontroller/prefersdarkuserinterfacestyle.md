# prefersDarkUserInterfaceStyle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the system draws the user interface in Dark Mode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var prefersDarkUserInterfaceStyle: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL prefersDarkUserInterfaceStyle;
```

## Discussion

To adopt the dark user interface style, set this value to [`true`](../../Swift/true.md) before you provide the root template or push any templates. The default value is [`false`](../../Swift/false.md), which allows templates to change between light and dark styles.

## See Also

### Configuring the Interface Controller
- [var delegate: (any CPInterfaceControllerDelegate)?](./delegate.md)
  An object that serves as the delegate to the interface controller.
- [protocol CPInterfaceControllerDelegate](../cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./setroottemplate%28_,animated,completion%29.md)
  Sets the root template of the navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller/prefersdarkuserinterfacestyle)*