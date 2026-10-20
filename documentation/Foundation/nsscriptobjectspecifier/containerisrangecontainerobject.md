# containerIsRangeContainerObject

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var containerIsRangeContainerObject: Bool { get set }
```

```objc
@property BOOL containerIsRangeContainerObject;
```

#### Discussion

If the receiver’s container specifier is `nil` and `flag` is [`true`](../../Swift/true.md), sets the receiver’s container to be the container for a range specifier. If the receiver’s container specifier is `nil` and `flag` is [`false`](../../Swift/false.md), sets the receiver’s container to be the top-level object.

If `flag` is [`true`](../../Swift/true.md), [`containerIsObjectBeingTested`](./containerisobjectbeingtested.md) should not also be invoked with an argument of [`true`](../../Swift/true.md).

## See Also

### Getting, testing, and setting containers
- [var containerClassDescription: NSScriptClassDescription?](./containerclassdescription.md)
  Sets the class description of the receiver’s container specifier to a given specifier.
- [var containerIsObjectBeingTested: Bool](./containerisobjectbeingtested.md)
  Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [var container: NSScriptObjectSpecifier?](./container.md)
  Sets the container specifier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/containerisrangecontainerobject)*