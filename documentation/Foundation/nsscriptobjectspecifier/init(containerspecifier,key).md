# init(containerSpecifier:key:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSScriptObjectSpecifier` object initialized with a given container specifier  and key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
convenience init(containerSpecifier container: NSScriptObjectSpecifier, key property: String)
```

```objc
- (instancetype) initWithContainerSpecifier:(NSScriptObjectSpecifier *) container key:(NSString *) property;
```

#### Return Value

An `NSScriptObjectSpecifier` object  initialized with container specifier `specifier` and key `key`.

#### Discussion

The class description of the container is set automatically.

## See Also

### Initializing an object specifier
- [init(containerClassDescription: NSScriptClassDescription, containerSpecifier: NSScriptObjectSpecifier?, key: String)](./init%28containerclassdescription,containerspecifier,key%29.md)
  Returns an `NSScriptObjectSpecifier` object initialized with the given attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/init(containerspecifier:key:))*