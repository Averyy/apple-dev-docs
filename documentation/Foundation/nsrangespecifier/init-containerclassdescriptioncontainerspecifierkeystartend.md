# init(containerClassDescription:containerSpecifier:key:start:end:)

**Framework**: Foundation  
**Kind**: init

Returns a range specifier initialized with the given properties.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, start startSpec: NSScriptObjectSpecifier?, end endSpec: NSScriptObjectSpecifier?)
```

#### Return Value

A range specifier initialized with the given properties.

#### Discussion

Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:).md) method and initializes the instance with the object specifiers representing the starting element, `startSpec`, and the ending element, `endSpec`, of a range of elements in the container.

## Parameters

- `classDesc`: The class description.
- `container`: The container.
- `property`: The property.
- `startSpec`: The object specifier representing the first object of the range.
- `endSpec`: The object specifier representing the last object of the range.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrangespecifier/init(containerclassdescription:containerspecifier:key:start:end:))*