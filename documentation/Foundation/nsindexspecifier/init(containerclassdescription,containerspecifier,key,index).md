# init(containerClassDescription:containerSpecifier:key:index:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an allocated [`NSIndexSpecifier`](../nsindexspecifier.md) object with a class description, container specifier, collection key, and object index.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, index: Int)
```

```objc
- (instancetype) initWithContainerClassDescription:(NSScriptClassDescription *) classDesc containerSpecifier:(NSScriptObjectSpecifier *) container key:(NSString *) property index:(NSInteger) index;
```

#### Return Value

Initialized [`NSIndexSpecifier`](../nsindexspecifier.md) object with its `index` property set to `objectIndex`.

#### Discussion

Invokes the super class’s [`init(containerClassDescription:containerSpecifier:key:)`](../nsscriptobjectspecifier/init%28containerclassdescription,containerspecifier,key%29.md) method and sets the `index` property of the index specifier to `objectIndex`.

## Parameters

- `classDesc`: Description for the container of the collection.
- `container`: Container of the collection.
- `property`: Name of the collection.
- `index`: The object within the `key` collection the index specifier is to identify.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexspecifier/init(containerclassdescription:containerspecifier:key:index:))*