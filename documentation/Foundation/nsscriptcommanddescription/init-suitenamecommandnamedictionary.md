# init(suiteName:commandName:dictionary:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns a newly allocated instance of `NSScriptCommandDescription`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(suiteName: String, commandName: String, dictionary commandDeclaration: [AnyHashable : Any]?)
```

#### Return Value

The initialized command description instance. Returns `nil` if the event constant or class name for the command description is missing; also returns `nil` if the return type or argument values are of the wrong type.

#### Discussion

This method registers `self` with the application’s global instance of [`NSScriptSuiteRegistry`](nsscriptsuiteregistry.md) and also registers all command arguments with the registry.

## Parameters

- `suiteName`: The name of the suite (in the application’s scriptability information) that the command belongs to. For example,  .
- `commandName`: The name of the script command that this instance describes.
- `commandDeclaration`: A command declaration dictionary of the sort that is valid in script suite property list files. This dictionary provides information about the command such as its argument names and types and return type (if any).

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/init(suitename:commandname:dictionary:))*