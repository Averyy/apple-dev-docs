# init(containerClassDescription:containerSpecifier:key:index:)

**Framework**: Foundation  
**Kind**: init

Initializes an allocated [`NSIndexSpecifier`](nsindexspecifier.md) object with a class description, container specifier, collection key, and object index.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, index: Int)
```

#### Return Value

Initialized [`NSIndexSpecifier`](nsindexspecifier.md) object with its `index` property set to `objectIndex`.

#### Discussion

Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:).md) method and sets the `index` property of the index specifier to `objectIndex`.

## Parameters

- `classDesc`: Description for the container of the collection.
- `container`: Container of the collection.
- `property`: Name of the collection.
- `index`: The object within the   collection the index specifier is to identify.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexspecifier/init(containerclassdescription:containerspecifier:key:index:))*