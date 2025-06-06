# nodeName

**Framework**: Open Directory  
**Kind**: property

The node’s name.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
var nodeName: String! { get }
```

## See Also

- [func customCall(Int, send: Data!) throws -> Data](odnode/customcall(_:send:).md)
  Returns the result of a custom call to the node.
- [func nodeDetails(forKeys: [Any]!) throws -> [AnyHashable : Any]](odnode/nodedetails(forkeys:).md)
  Returns a dictionary containing details about a node.
- [func subnodeNames() throws -> [Any]](odnode/subnodenames.md)
  Returns the names of subnodes for the node.
- [func unreachableSubnodeNames() throws -> [Any]](odnode/unreachablesubnodenames.md)
  Returns an array of the subnodes of a given node that are currently unreachable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/nodename)*