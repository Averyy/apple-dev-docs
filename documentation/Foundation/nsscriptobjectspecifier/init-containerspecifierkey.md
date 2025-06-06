# init(containerSpecifier:key:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSScriptObjectSpecifier` object initialized with a given container specifier  and key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(containerSpecifier container: NSScriptObjectSpecifier, key property: String)
```

#### Return Value

An `NSScriptObjectSpecifier` object  initialized with container specifier `specifier` and key `key`.

#### Discussion

The class description of the container is set automatically.

## See Also

- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String)](nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:).md)
  Returns an `NSScriptObjectSpecifier` object initialized with the given attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(containerspecifier:key:))*