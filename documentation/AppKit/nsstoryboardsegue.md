# NSStoryboardSegue

**Framework**: AppKit  
**Kind**: class

A transition or containment relationship between two scenes in a storyboard.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class NSStoryboardSegue
```

#### Overview

In this context, a  is a view controller or a window controller and a  is an instance of the [`NSStoryboard`](nsstoryboard.md) class.

A storyboard segue has a procedural notion of being invoked, known in the API as being . You can take advantage of hooks into the segue performance process by way of the [`NSSeguePerforming`](nssegueperforming.md) protocol.

You do not create storyboard segue objects directly. Instead, the system creates them as needed as segues are invoked. To run code during initialization and performance of a segue, override the [`init(identifier:source:destination:)`](nsstoryboardsegue/init(identifier:source:destination:).md) and [`perform()`](nsstoryboardsegue/perform().md) methods.

You can initiate a segue programmatically with the [`performSegue(withIdentifier:sender:)`](nssegueperforming/performsegue(withidentifier:sender:).md) method of the [`NSSeguePerforming`](nssegueperforming.md) protocol. For example, you might do this to transition from a scene in one storyboard file to a scene in another.

## Topics

### Inspecting a Storyboard Segue
- [var sourceController: Any](nsstoryboardsegue/sourcecontroller.md)
  The starting/containing view controller or window controller for the storyboard segue.
- [var destinationController: Any](nsstoryboardsegue/destinationcontroller.md)
  The ending/contained view controller or window controller for the storyboard segue.
- [var identifier: NSStoryboardSegue.Identifier?](nsstoryboardsegue/identifier-swift.property.md)
  An optional, unique identifier for the storyboard segue that you can specify using the Identity inspector in Interface Builder.
- [NSStoryboardSegue.Identifier](nsstoryboardsegue/identifier-swift.typealias.md)
### Customizing Storyboard Segue Initialization and Invocation
- [convenience init(identifier: NSStoryboardSegue.Identifier, source: Any, destination: Any, performHandler: () -> Void)](nsstoryboardsegue/init(identifier:source:destination:performhandler:).md)
  Creates a storyboard segue and a block used when the segue is performed.
- [init(identifier: NSStoryboardSegue.Identifier, source: Any, destination: Any)](nsstoryboardsegue/init(identifier:source:destination:).md)
  The designated initializer for a storyboard segue.
- [func perform()](nsstoryboardsegue/perform.md)
  Performs a visual transition from one controller to another.

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

- [class NSStoryboard](nsstoryboard.md)
  An encapsulation of the design-time view controller and window controller graph represented in an Interface Builder storyboard resource file.
- [protocol NSSeguePerforming](nssegueperforming.md)
  A set of methods that support the mediation of a custom segue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstoryboardsegue)*