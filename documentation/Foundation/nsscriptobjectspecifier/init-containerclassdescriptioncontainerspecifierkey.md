# init(containerClassDescription:containerSpecifier:key:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSScriptObjectSpecifier` object initialized with the given attributes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String)
```

#### Return Value

An `NSScriptObjectSpecifier` object initialized with container specifier `specifier`, key `key`, and the class description of the object specifier `classDescription`, derived from the value of the specifier’s key.

#### Discussion

You should never pass `nil` for the value of `classDescription`. The receiver’s child reference is set to `nil`.

This is the designated initializer for `NSScriptObjectSpecifier`.

## See Also

- [convenience init(containerSpecifier: NSScriptObjectSpecifier, key: String)](nsscriptobjectspecifier/init(containerspecifier:key:).md)
  Returns an `NSScriptObjectSpecifier` object initialized with a given container specifier  and key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(containerclassdescription:containerspecifier:key:))*