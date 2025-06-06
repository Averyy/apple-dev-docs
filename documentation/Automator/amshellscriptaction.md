# AMShellScriptAction

**Framework**: Automator  
**Kind**: class

An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMShellScriptAction
```

#### Overview

When you create a Shell Script Automator Action project in Xcode, the project template supplies an [`AMShellScriptAction`](amshellscriptaction.md) instance as the Principal Class of the action bundle. This ready-made instance provides a default implementation of the [`AMAction`](amaction.md) [`run(withInput:)`](amaction/run(withinput:).md) method that uses the logic defined in the script. You can substitute your own subclass of [`AMShellScriptAction`](amshellscriptaction.md) for Principal Class if you need to.

## Topics

### Handling the I/O Separator Character
- [var inputFieldSeparator: String](amshellscriptaction/inputfieldseparator.md)
  A string to use as the delimiter between items in the string passed to the action through standard input.
- [var outputFieldSeparator: String](amshellscriptaction/outputfieldseparator.md)
  A string to use as a delimiter in the string output by the action.
- [var remapLineEndings: Bool](amshellscriptaction/remaplineendings.md)
  A Boolean value that indicates whether you want automatic remapping of carriage return (`\r`) to newline (`\n`) characters in the input string.

## Relationships

### Inherits From
- [AMBundleAction](ambundleaction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class AMBundleAction](ambundleaction.md)
  An object that represents an Automator action that’s a loadable bundle.
- [class AMAction](amaction.md)
  An abstract class that defines the interface and general characteristics of Automator actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amshellscriptaction)*