# AMAppleScriptAction

**Framework**: Automator  
**Kind**: class  
**Role**: Class

An object that represents Automator actions whose runtime behavior is driven by an AppleScript script.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

> **Deprecated**: Use the Cocoa-AppleScript template (an instance of [`AMBundleAction`](./ambundleaction.md)) in Xcode to create AppleScript-based Automator actions.

## Declaration

```swift
class AMAppleScriptAction
```

```objc
@interface AMAppleScriptAction : AMBundleAction
```

## Overview

An [`AMAppleScriptAction`](./amapplescriptaction.md) object holds the compiled script as an instance of the `OSAScript` class. By default, the `OSAScript` object is instantiated from the script in the Xcode project file `main.applescript`.

When you create a Automator Applescript Action project in Xcode, the project template supplies an [`AMAppleScriptAction`](./amapplescriptaction.md) instance as File’s Owner of the action bundle. This ready-made instance provides a default implementation of the [`AMAction`](./amaction.md) [`run(withInput:)`](./amaction/run%28withinput%29.md) method that uses the logic defined in the script. You can substitute your own subclass of [`AMAppleScriptAction`](./amapplescriptaction.md) for File’s Owner if you need to.

## Topics

### Accessing the script
- [var script: OSAScript?](./amapplescriptaction/script.md)
  An `OSAScript` object representing the receiver’s script containing the `on run` command handler.

## Relationships

### Inherits From
- [AMBundleAction](./ambundleaction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amapplescriptaction)*