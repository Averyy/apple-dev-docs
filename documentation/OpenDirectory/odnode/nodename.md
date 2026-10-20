# nodeName

**Framework**: Open Directory  
**Kind**: property  
**Role**: Instance Property

The node’s name.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
var nodeName: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * nodeName;
```

## See Also

### Querying a Node
- [func customCall(Int, send: Data!) throws -> Data](./customcall%28_,send%29.md)
  Returns the result of a custom call to the node.
- [func nodeDetails(forKeys: [Any]!) throws -> [AnyHashable : Any]](./nodedetails%28forkeys%29.md)
  Returns a dictionary containing details about a node.
- [func subnodeNames() throws -> [Any]](./subnodenames%28%29.md)
  Returns the names of subnodes for the node.
- [func unreachableSubnodeNames() throws -> [Any]](./unreachablesubnodenames%28%29.md)
  Returns an array of the subnodes of a given node that are currently unreachable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/nodename)*