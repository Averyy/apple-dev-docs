# init(containerClassDescription:containerSpecifier:key:relativePosition:baseSpecifier:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](../nsscriptobjectspecifier/init%28containerclassdescription,containerspecifier,key%29.md) method and initializes the relative position and base specifier to `relPos` and `baseSpecifier`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, relativePosition relPos: NSRelativeSpecifier.RelativePosition, baseSpecifier: NSScriptObjectSpecifier?)
```

```objc
- (instancetype) initWithContainerClassDescription:(NSScriptClassDescription *) classDesc containerSpecifier:(NSScriptObjectSpecifier *) container key:(NSString *) property relativePosition:(NSRelativePosition) relPos baseSpecifier:(NSScriptObjectSpecifier *) baseSpecifier;
```

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrelativespecifier/init(containerclassdescription:containerspecifier:key:relativeposition:basespecifier:))*