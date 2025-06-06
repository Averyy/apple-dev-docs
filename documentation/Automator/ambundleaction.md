# AMBundleAction

**Framework**: Automator  
**Kind**: class

An object that represents an Automator action that’s a loadable bundle.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMBundleAction
```

#### Overview

Automator loads action bundles from standard locations in the file system: `/System/Library/Automator`, `/Library/Automator`, and `~/Library/Automator`.

[`AMBundleAction`](ambundleaction.md) objects have several important properties:

- The [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) object associated with the action’s physical bundle
- The action’s view, which holds its user interface
- A parameters dictionary that reflects the settings in the user interface

When you create a Cocoa Automator Action project in Xcode, the project template includes a custom subclass of [`AMBundleAction`](ambundleaction.md). This custom class uses the name of the project.

You must provide an implementation of [`run(withInput:)`](amaction/run(withinput:).md), which is declared by the superclass [`AMAction`](amaction.md). If you add any instance variables, you must override the [`init(definition:fromArchive:)`](amaction/init(definition:fromarchive:).md) method and the [`write(to:)`](amaction/write(to:).md) method of [`AMAction`](amaction.md) to work with them.

## Topics

### Initializing the Action
- [func awakeFromBundle()](ambundleaction/awakefrombundle.md)
  Allows the action object to perform setup tasks requiring the presence of all bundle objects.
### Managing Action Properties
- [var bundle: Bundle](ambundleaction/bundle.md)
  The action’s bundle object.
- [var hasView: Bool](ambundleaction/hasview.md)
  A Boolean value that indicates whether the action has a view associated with it.
- [var view: NSView?](ambundleaction/view.md)
  The action’s view object.
- [var parameters: NSMutableDictionary?](ambundleaction/parameters.md)
  The action’s parameters.

## Relationships

### Inherits From
- [AMAction](amaction.md)
### Inherited By
- [AMAppleScriptAction](amapplescriptaction.md)
- [AMShellScriptAction](amshellscriptaction.md)
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

- [class AMShellScriptAction](amshellscriptaction.md)
  An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.
- [class AMAction](amaction.md)
  An abstract class that defines the interface and general characteristics of Automator actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/ambundleaction)*