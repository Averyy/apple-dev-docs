# ScreenSaverDefaults

**Framework**: Screen Saver  
**Kind**: class

A class that defines a set of methods for saving and restoring user defaults for screen savers.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class ScreenSaverDefaults
```

#### Overview

[`ScreenSaverDefaults`](screensaverdefaults.md) gives you access to preference values you need to configure your screen saver. Because multiple apps can load a screen saver, you can’t use the standard [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) object to store preferences. Instead, instantiate this class using the [`init(forModuleWithName:)`](screensaverdefaults/init(formodulewithname:).md) method, which takes your screen saver’s bundle identifier as a parameter. The resulting object gives you a way to store your preference values and associate them only with your screen saver. Use the inherited [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) methods to load, store, or modify values.

## Topics

### Creating the screen saver defaults
- [convenience init?(forModuleWithName: String)](screensaverdefaults/init(formodulewithname:).md)
  Returns a screen saver defaults instance that reads and writes defaults for the specified module.

## Relationships

### Inherits From
- [UserDefaults](../Foundation/UserDefaults.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ScreenSaverView](screensaverview.md)
  An abstract class that defines the interface for subclassers to interact with the screen saver infrastructure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverdefaults)*