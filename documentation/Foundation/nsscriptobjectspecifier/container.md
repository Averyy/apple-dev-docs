# container

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the container specifier of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var container: NSScriptObjectSpecifier? { get set }
```

```objc
@property (retain, nullable) NSScriptObjectSpecifier * containerSpecifier;
```

## Parameters

- `objSpecifier`: The container specifier for the receiver.

## See Also

### Getting, testing, and setting containers
- [var containerClassDescription: NSScriptClassDescription?](./containerclassdescription.md)
  Sets the class description of the receiver’s container specifier to a given specifier.
- [var containerIsObjectBeingTested: Bool](./containerisobjectbeingtested.md)
  Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [var containerIsRangeContainerObject: Bool](./containerisrangecontainerobject.md)
  Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/container)*