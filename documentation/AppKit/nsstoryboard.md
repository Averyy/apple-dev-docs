# NSStoryboard

**Framework**: AppKit  
**Kind**: class

An encapsulation of the design-time view controller and window controller graph represented in an Interface Builder storyboard resource file.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSStoryboard
```

#### Overview

You can use storyboard files to define the view and window controllers for all or part of an app’s user interface. Typically, AppKit creates these objects automatically in response to actions defined within a storyboard file itself, such as the clicking of a button or the choosing of a menu item. However, you can use a storyboard object to directly instantiate the initial view controller from a storyboard file or to instantiate other view or window controllers that you want to present programmatically. In the context of a storyboard file, each contained controller is called a .

A transition from one scene to another in a storyboard is called a . This same term, and the same Cocoa APIs, express a containment relationship between two scenes. In macOS, containment (rather than transition) is the more common notion for storyboards. For descriptions of the related APIs, refer to [`NSStoryboardSegue`](nsstoryboardsegue.md) and [`NSSeguePerforming`](nssegueperforming.md).

## Topics

### Creating a Storyboard Object
- [convenience init(name: NSStoryboard.Name, bundle: Bundle?)](nsstoryboard/init(name:bundle:).md)
  Creates a storyboard based on the named storyboard file in the specified bundle.
- [class var main: NSStoryboard?](nsstoryboard/main.md)
  The app’s main storyboard.
- [NSStoryboard.Name](nsstoryboard/name.md)
  The name of the storyboard file.
### Loading the Initial View Controller
- [func instantiateInitialController() -> Any?](nsstoryboard/instantiateinitialcontroller.md)
  Creates the initial view controller or window controller from a storyboard.
- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](nsstoryboard/instantiateinitialcontroller(creator:)-pi04.md)
  Creates the initial view controller from the storyboard and initializes it using your custom code.
- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](nsstoryboard/instantiateinitialcontroller(creator:)-529r1.md)
  Creates the initial window controller from the storyboard and initializes it using your custom code.
### Instantiating Storyboard Controllers
- [func instantiateController(withIdentifier: NSStoryboard.SceneIdentifier) -> Any](nsstoryboard/instantiatecontroller(withidentifier:).md)
  Instantiates a specified view controller or window controller from a storyboard.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](nsstoryboard/instantiatecontroller(identifier:creator:)-7ddcf.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](nsstoryboard/instantiatecontroller(identifier:creator:)-50rw3.md)
  Creates the specified window controller from the storyboard and initializes it using your custom initialization code.
- [NSStoryboard.SceneIdentifier](nsstoryboard/sceneidentifier.md)
  A string that uniquely identifies a view controller or window controller in your storyboard file.

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

- [class NSStoryboardSegue](nsstoryboardsegue.md)
  A transition or containment relationship between two scenes in a storyboard.
- [protocol NSSeguePerforming](nssegueperforming.md)
  A set of methods that support the mediation of a custom segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard)*