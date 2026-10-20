# ScreenSaverDefaults

**Framework**: Screen Saver  
**Kind**: class  
**Role**: Class

A class that defines a set of methods for saving and restoring user defaults for screen savers.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class ScreenSaverDefaults
```

```objc
@interface ScreenSaverDefaults : NSUserDefaults
```

#### Overview

[`ScreenSaverDefaults`](./screensaverdefaults.md) gives you access to preference values you need to configure your screen saver. Because multiple apps can load a screen saver, you can’t use the standard [`UserDefaults`](../Foundation/userdefaults.md) object to store preferences. Instead, instantiate this class using the [`init(forModuleWithName:)`](./screensaverdefaults/init%28formodulewithname%29.md) method, which takes your screen saver’s bundle identifier as a parameter. The resulting object gives you a way to store your preference values and associate them only with your screen saver. Use the inherited [`UserDefaults`](../Foundation/userdefaults.md) methods to load, store, or modify values.

## Topics

### Creating the screen saver defaults
- [convenience init?(forModuleWithName: String)](./screensaverdefaults/init%28formodulewithname%29.md)
  Returns a screen saver defaults instance that reads and writes defaults for the specified module.

## Relationships

### Inherits From
- [UserDefaults](../Foundation/userdefaults.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Interface
- [class ScreenSaverView](./screensaverview.md)
  An abstract class that defines the interface for subclassers to interact with the screen saver infrastructure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverdefaults)*