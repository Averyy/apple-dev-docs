# NSAccessibilityCustomAction

**Framework**: AppKit  
**Kind**: class

A custom action to perform on an accessible object.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class NSAccessibilityCustomAction
```

#### Overview

Apps that support custom actions can create instances of this class, specifying the user-readable name of the action, and either a handler closure or the object and selector to use when performing the action. Assistive apps display custom actions in response to specific user cues. For example, VoiceOver lets users access actions quickly using the Actions rotor.

After creating an instance of this class, add it to the [`accessibilityCustomActions`](nsaccessibility-c.protocol/accessibilitycustomactions.md) property of an appropriate accessible object.

## Topics

### Creating a Custom Action
- [init(name: String, handler: (() -> Bool)?)](nsaccessibilitycustomaction/init(name:handler:).md)
  Creates a custom action object with the specified name and handler.
- [init(name: String, target: any NSObjectProtocol, selector: Selector)](nsaccessibilitycustomaction/init(name:target:selector:).md)
  Creates a custom action object with the specified name, target, and selector.
### Getting the Action Name
- [var name: String](nsaccessibilitycustomaction/name.md)
  A localized name that describes the action.
### Getting the Action
- [var handler: (() -> Bool)?](nsaccessibilitycustomaction/handler.md)
  The closure that handles the execution of the action.
- [var target: (any NSObjectProtocol)?](nsaccessibilitycustomaction/target.md)
  The object that performs the action through a selector.
- [var selector: Selector?](nsaccessibilitycustomaction/selector.md)
  The method to call on the target to perform the action.

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

- [func accessibilityCustomActions() -> [NSAccessibilityCustomAction]?](nsaccessibilityprotocol/accessibilitycustomactions.md)
  Returns the custom actions of the current accessibility element.
- [func setAccessibilityCustomActions([NSAccessibilityCustomAction]?)](nsaccessibilityprotocol/setaccessibilitycustomactions(_:).md)
  Sets the custom actions of the current accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomaction)*