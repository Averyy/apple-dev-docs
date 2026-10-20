# CPInterfaceControllerDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol CPInterfaceControllerDelegate <NSObject>
```

## Topics

### Handling Display Events
- [func templateWillAppear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatewillappear%28_,animated%29.md)
  Tells the delegate that the template will appear onscreen.
- [func templateDidAppear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatedidappear%28_,animated%29.md)
  Tells the delegate that the template did appear onscreen.
- [func templateWillDisappear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatewilldisappear%28_,animated%29.md)
  Tells the delegate that the template will disappear from the screen.
- [func templateDidDisappear(CPTemplate, animated: Bool)](./cpinterfacecontrollerdelegate/templatediddisappear%28_,animated%29.md)
  Tells the delegate that the template did disappear from the screen.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring the Interface Controller
- [var delegate: (any CPInterfaceControllerDelegate)?](./cpinterfacecontroller/delegate.md)
  An object that serves as the delegate to the interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](./cpinterfacecontroller/prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](./cpinterfacecontroller/setroottemplate%28_,animated,completion%29.md)
  Sets the root template of the navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontrollerdelegate)*