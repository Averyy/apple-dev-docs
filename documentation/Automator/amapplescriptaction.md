# AMAppleScriptAction

**Framework**: Automator  
**Kind**: class

An object that represents Automator actions whose runtime behavior is driven by an AppleScript script.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMAppleScriptAction
```

#### Overview

An [`AMAppleScriptAction`](amapplescriptaction.md) object holds the compiled script as an instance of the `OSAScript` class. By default, the `OSAScript` object is instantiated from the script in the Xcode project file `main.applescript`.

When you create a Automator Applescript Action project in Xcode, the project template supplies an [`AMAppleScriptAction`](amapplescriptaction.md) instance as File’s Owner of the action bundle. This ready-made instance provides a default implementation of the [`AMAction`](amaction.md) [`run(withInput:)`](amaction/run(withinput:).md) method that uses the logic defined in the script. You can substitute your own subclass of [`AMAppleScriptAction`](amapplescriptaction.md) for File’s Owner if you need to.

## Topics

### Accessing the script
- [var script: OSAScript?](amapplescriptaction/script.md)
  An `OSAScript` object representing the receiver’s script containing the `on run` command handler.

## Relationships

### Inherits From
- [AMBundleAction](ambundleaction.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amapplescriptaction)*