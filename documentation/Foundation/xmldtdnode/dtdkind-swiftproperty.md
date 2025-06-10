# dtdKind

**Framework**: Foundation  
**Kind**: property

Returns the receiver’s DTD kind.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var dtdKind: XMLDTDNode.DTDKind { get set }
```

#### Return Value

The receiver’s DTD kind. See Constants for a list of valid NSXMLDTDNodeKind constants.

#### Discussion

The DTD kind is distinct from a `NSXMLDTDNode` object’s node kind (returned by the `NSXMLNode` [`kind`](xmlnode/kind-swift.property.md) method).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.property)*