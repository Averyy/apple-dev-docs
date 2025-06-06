# init(commandDescription:)

**Framework**: Foundation  
**Kind**: init

Returns an a script command object initialized from the passed command description.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(commandDescription commandDef: NSScriptCommandDescription)
```

#### Return Value

A newly initialized instance of `NSScriptCommand` or a subclass.

#### Discussion

To make this command object usable, you must set its receiving objects and arguments (if any) after invoking this method.

## Parameters

- `commandDef`: A command description for the command to be created.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [var receiversSpecifier: NSScriptObjectSpecifier?](nsscriptcommand/receiversspecifier.md)
  Sets the object specifier to `receiversSpec` that, when evaluated, indicates the receiver or receivers of the command.
- [var arguments: [String : Any]?](nsscriptcommand/arguments.md)
  Sets the arguments of the command to `args`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/init(commanddescription:))*