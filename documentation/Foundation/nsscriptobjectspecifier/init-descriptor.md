# init(descriptor:)

**Framework**: Foundation  
**Kind**: init

Returns a new object specifier for an Apple event descriptor.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(descriptor: NSAppleEventDescriptor)
```

#### Return Value

An object specifier, or `nil` if an error occurs.

#### Discussion

If `objectSpecifierWithDescriptor:` is invoked and fails during the execution of a script command, information about the error that caused the failure is recorded in `[NSScriptCommand currentCommand]`.

## Parameters

- `descriptor`: An Apple event descriptor. The descriptor must have the type  .

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(descriptor:))*