# AMBundleAction

**Framework**: Automator  
**Kind**: class  
**Role**: Class

An object that represents an Automator action that’s a loadable bundle.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMBundleAction
```

```objc
@interface AMBundleAction : AMAction
```

## Overview

Automator loads action bundles from standard locations in the file system: `/System/Library/Automator`, `/Library/Automator`, and `~/Library/Automator`.

[`AMBundleAction`](./ambundleaction.md) objects have several important properties:

- The [`Bundle`](../Foundation/bundle.md) object associated with the action’s physical bundle
- The action’s view, which holds its user interface
- A parameters dictionary that reflects the settings in the user interface

When you create a Cocoa Automator Action project in Xcode, the project template includes a custom subclass of [`AMBundleAction`](./ambundleaction.md). This custom class uses the name of the project.

You must provide an implementation of [`run(withInput:)`](./amaction/run%28withinput%29.md), which is declared by the superclass [`AMAction`](./amaction.md). If you add any instance variables, you must override the [`init(definition:fromArchive:)`](./amaction/init%28definition,fromarchive%29.md) method and the [`write(to:)`](./amaction/write%28to%29.md) method of [`AMAction`](./amaction.md) to work with them.

## Topics

### Initializing the Action
- [func awakeFromBundle()](./ambundleaction/awakefrombundle%28%29.md)
  Allows the action object to perform setup tasks requiring the presence of all bundle objects.
### Managing Action Properties
- [var bundle: Bundle](./ambundleaction/bundle.md)
  The action’s bundle object.
- [var hasView: Bool](./ambundleaction/hasview.md)
  A Boolean value that indicates whether the action has a view associated with it.
- [var view: NSView?](./ambundleaction/view.md)
  The action’s view object.
- [var parameters: NSMutableDictionary?](./ambundleaction/parameters.md)
  The action’s parameters.
### Initializers
- [init?(coder: NSCoder)](./ambundleaction/init%28coder%29.md)

## Relationships

### Inherits From
- [AMAction](./amaction.md)
### Inherited By
- [AMAppleScriptAction](./amapplescriptaction.md)
- [AMShellScriptAction](./amshellscriptaction.md)
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

## See Also

### Actions
- [class AMShellScriptAction](./amshellscriptaction.md)
  An object that represents Automator actions whose runtime behavior is driven by a shell script or by a Perl or Python script.
- [class AMAction](./amaction.md)
  An abstract class that defines the interface and general characteristics of Automator actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/ambundleaction)*