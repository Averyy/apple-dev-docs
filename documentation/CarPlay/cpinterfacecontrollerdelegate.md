# CPInterfaceControllerDelegate

**Framework**: CarPlay  
**Kind**: protocol

The interface that an object implements to serve as a delegate to an interface controller.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol CPInterfaceControllerDelegate : NSObjectProtocol
```

## Topics

### Handling Display Events
- [func templateWillAppear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatewillappear(_:animated:).md)
  Tells the delegate that the template will appear onscreen.
- [func templateDidAppear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatedidappear(_:animated:).md)
  Tells the delegate that the template did appear onscreen.
- [func templateWillDisappear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatewilldisappear(_:animated:).md)
  Tells the delegate that the template will disappear from the screen.
- [func templateDidDisappear(CPTemplate, animated: Bool)](cpinterfacecontrollerdelegate/templatediddisappear(_:animated:).md)
  Tells the delegate that the template did disappear from the screen.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CPInterfaceControllerDelegate)?](cpinterfacecontroller/delegate.md)
  An object that serves as the delegate to the interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](cpinterfacecontroller/prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/setroottemplate(_:animated:completion:).md)
  Sets the root template of the navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate)*