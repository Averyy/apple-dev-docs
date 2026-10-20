# containerClassDescription

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the class description of the receiver’s container specifier to a given specifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var containerClassDescription: NSScriptClassDescription? { get set }
```

```objc
@property (retain, nullable) NSScriptClassDescription * containerClassDescription;
```

## Parameters

- `classDescription`: The class description of the receiver’s container specifier.

## See Also

### Getting, testing, and setting containers
- [var containerIsObjectBeingTested: Bool](./containerisobjectbeingtested.md)
  Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [var containerIsRangeContainerObject: Bool](./containerisrangecontainerobject.md)
  Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.
- [var container: NSScriptObjectSpecifier?](./container.md)
  Sets the container specifier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/containerclassdescription)*