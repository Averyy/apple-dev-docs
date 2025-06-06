# init(containerClassDescription:containerSpecifier:key:test:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSWhoseSpecifier` object initialized with the given attributes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, test: NSScriptWhoseTest)
```

#### Return Value

An `NSWhoseSpecifier` object initialized with the given attributes.

#### Discussion

Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:).md) and sets the whose test condition to `test`.

## Parameters

- `classDesc`: Class description for the receiver’s container object.
- `container`: An object specifier for the receiver’s container object.
- `property`: The key for the property for which to test.
- `test`: The test condition.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswhosespecifier/init(containerclassdescription:containerspecifier:key:test:))*