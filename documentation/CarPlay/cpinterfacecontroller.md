# CPInterfaceController

**Framework**: CarPlay  
**Kind**: class

A controller that manages the templates for constructing a scene’s user interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPInterfaceController
```

#### Overview

An interface controller manages one or more templates in the navigation hierarchy. You don’t create the interface controller. Instead, CarPlay creates one for you and passes it to the delegate of [`CPTemplateApplicationScene`](cptemplateapplicationscene.md) when the scene connects.

After receiving the controller, store a reference to it in your app. Then set the root template by calling the [`setRootTemplate(_:animated:completion:)`](cpinterfacecontroller/setroottemplate(_:animated:completion:).md) method. To display another template in the navigation hierarchy, call [`pushTemplate(_:animated:completion:)`](cpinterfacecontroller/pushtemplate(_:animated:completion:).md), and use [`popTemplate(animated:completion:)`](cpinterfacecontroller/poptemplate(animated:completion:).md) to remove the top-most template.

You also use the interface controller to display a single template modally. Call [`presentTemplate(_:animated:completion:)`](cpinterfacecontroller/presenttemplate(_:animated:completion:).md) to display the modal template, and call [`dismissTemplate(animated:completion:)`](cpinterfacecontroller/dismisstemplate(animated:completion:).md) to dismiss it.

## Topics

### Configuring the Interface Controller
- [var delegate: (any CPInterfaceControllerDelegate)?](cpinterfacecontroller/delegate.md)
  An object that serves as the delegate to the interface controller.
- [protocol CPInterfaceControllerDelegate](cpinterfacecontrollerdelegate.md)
  The interface that an object implements to serve as a delegate to an interface controller.
- [var prefersDarkUserInterfaceStyle: Bool](cpinterfacecontroller/prefersdarkuserinterfacestyle.md)
  A Boolean value that determines whether the system draws the user interface in Dark Mode.
- [func setRootTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/setroottemplate(_:animated:completion:).md)
  Sets the root template of the navigation hierarchy.
### Accessing the Trait Collection
- [var carTraitCollection: UITraitCollection](cpinterfacecontroller/cartraitcollection.md)
  The trait collection of the vehicle’s primary screen.
### Accessing Templates
- [var rootTemplate: CPTemplate](cpinterfacecontroller/roottemplate.md)
  The root template in the navigation hierarchy.
- [var topTemplate: CPTemplate?](cpinterfacecontroller/toptemplate.md)
  The top-most template in the navigation hierarchy.
- [var templates: [CPTemplate]](cpinterfacecontroller/templates.md)
  The contents of the navigation hierarchy.
### Adding and Removing Templates
- [func pushTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/pushtemplate(_:animated:completion:).md)
  Adds the specified template to the navigation hierarchy and displays it.
- [func popTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptemplate(animated:completion:).md)
  Removes the top-most template from the navigation hierarchy.
- [func popToRootTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/poptoroottemplate(animated:completion:).md)
  Removes all of the templates from the navigation hierarchy except the root template.
- [func pop(to: CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/pop(to:animated:completion:).md)
  Removes each template from the navigation hierarchy until the specified template becomes visible.
### Displaying Templates Modally
- [func presentTemplate(CPTemplate, animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/presenttemplate(_:animated:completion:).md)
  Presents a template modally.
- [func dismissTemplate(animated: Bool, completion: ((Bool, (any Error)?) -> Void)?)](cpinterfacecontroller/dismisstemplate(animated:completion:).md)
  Dismisses a modal template.
- [var presentedTemplate: CPTemplate?](cpinterfacecontroller/presentedtemplate.md)
  The interface controller’s current modal template.
### Deprecated
- [Deprecated Symbols](cpinterfacecontroller-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

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

- [var interfaceController: CPInterfaceController](cptemplateapplicationscene/interfacecontroller.md)
  The controller that manages the scene’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinterfacecontroller)*