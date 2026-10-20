# NSStoryboard

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An encapsulation of the design-time view controller and window controller graph represented in an Interface Builder storyboard resource file.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSStoryboard
```

```objc
@interface NSStoryboard : NSObject
```

#### Overview

You can use storyboard files to define the view and window controllers for all or part of an app’s user interface. Typically, AppKit creates these objects automatically in response to actions defined within a storyboard file itself, such as the clicking of a button or the choosing of a menu item. However, you can use a storyboard object to directly instantiate the initial view controller from a storyboard file or to instantiate other view or window controllers that you want to present programmatically. In the context of a storyboard file, each contained controller is called a *scene*.

A transition from one scene to another in a storyboard is called a *segue*. This same term, and the same Cocoa APIs, express a containment relationship between two scenes. In macOS, containment (rather than transition) is the more common notion for storyboards. For descriptions of the related APIs, refer to [`NSStoryboardSegue`](./nsstoryboardsegue.md) and [`NSSeguePerforming`](./nssegueperforming.md).

## Topics

### Creating a Storyboard Object
- [convenience init(name: NSStoryboard.Name, bundle: Bundle?)](./nsstoryboard/init%28name,bundle%29.md)
  Creates a storyboard based on the named storyboard file in the specified bundle.
- [class var main: NSStoryboard?](./nsstoryboard/main.md)
  The app’s main storyboard.
- [NSStoryboard.Name](./nsstoryboard/name.md)
  The name of the storyboard file.
### Loading the Initial View Controller
- [func instantiateInitialController() -> Any?](./nsstoryboard/instantiateinitialcontroller%28%29.md)
  Creates the initial view controller or window controller from a storyboard.
- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](./nsstoryboard/instantiateinitialcontroller%28creator%29-pi04.md)
  Creates the initial view controller from the storyboard and initializes it using your custom code.
- [func instantiateInitialController<Controller>(creator: ((NSCoder) -> Controller?)?) -> Controller?](./nsstoryboard/instantiateinitialcontroller%28creator%29-529r1.md)
  Creates the initial window controller from the storyboard and initializes it using your custom code.
### Instantiating Storyboard Controllers
- [func instantiateController(withIdentifier: NSStoryboard.SceneIdentifier) -> Any](./nsstoryboard/instantiatecontroller%28withidentifier%29.md)
  Instantiates a specified view controller or window controller from a storyboard.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](./nsstoryboard/instantiatecontroller%28identifier,creator%29-7ddcf.md)
  Creates the specified view controller from the storyboard and initializes it using your custom initialization code.
- [func instantiateController<Controller>(identifier: NSStoryboard.SceneIdentifier, creator: ((NSCoder) -> Controller?)?) -> Controller](./nsstoryboard/instantiatecontroller%28identifier,creator%29-50rw3.md)
  Creates the specified window controller from the storyboard and initializes it using your custom initialization code.
- [NSStoryboard.SceneIdentifier](./nsstoryboard/sceneidentifier.md)
  A string that uniquely identifies a view controller or window controller in your storyboard file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Storyboard
- [class NSStoryboardSegue](./nsstoryboardsegue.md)
  A transition or containment relationship between two scenes in a storyboard.
- [protocol NSSeguePerforming](./nssegueperforming.md)
  A set of methods that support the mediation of a custom segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboard)*