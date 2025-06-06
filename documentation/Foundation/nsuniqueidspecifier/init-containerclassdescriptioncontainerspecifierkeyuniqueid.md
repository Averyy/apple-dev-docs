# init(containerClassDescription:containerSpecifier:key:uniqueID:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSUniqueIDSpecifier` object, initialized with the given arguments.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, uniqueID: Any)
```

#### Return Value

An `NSUniqueIDSpecifier` object, initialized with the given arguments.

#### Discussion

Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:).md) method and sets the ID to `uniqueID`.

## Parameters

- `classDesc`: The class description for the new object.
- `container`: The container for the new object.
- `property`: The property for the new object.
- `uniqueID`:  must be an instance of   or  . The type should match the declared type of the attribute of the specified scriptable class whose four-character code is  .

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuniqueidspecifier/init(containerclassdescription:containerspecifier:key:uniqueid:))*