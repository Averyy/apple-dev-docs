# containerIsObjectBeingTested

**Framework**: Foundation  
**Kind**: property

Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var containerIsObjectBeingTested: Bool { get set }
```

#### Discussion

If the receiver’s container specifier is `nil` and `flag` is [`true`](https://developer.apple.com/documentation/Swift/true), sets the receiver’s container to be an object involved in a filter reference (for example, `whose color is blue`). If the receiver’s container specifier is `nil` and `flag` is [`false`](https://developer.apple.com/documentation/Swift/false), sets the receiver’s container to be the top-level object.

If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true) [`containerIsRangeContainerObject`](nsscriptobjectspecifier/containerisrangecontainerobject.md) should not also be invoked with an argument of [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var containerClassDescription: NSScriptClassDescription?](nsscriptobjectspecifier/containerclassdescription.md)
  Sets the class description of the receiver’s container specifier to a given specifier.
- [var containerIsRangeContainerObject: Bool](nsscriptobjectspecifier/containerisrangecontainerobject.md)
  Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.
- [var container: NSScriptObjectSpecifier?](nsscriptobjectspecifier/container.md)
  Sets the container specifier of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/containerisobjectbeingtested)*