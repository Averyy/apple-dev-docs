# SecTransformMetaAttributeType.canCycle

**Framework**: Security  
**Kind**: case

The transform allows cyclic behavior.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case canCycle
```

#### Discussion

A transform group is a directed graph which is typically acyclic. Some transforms need to work with cycles. For example, a transform that emits a header and trailer around the data of another transform must create a cycle. If this metadata set to [`true`](https://developer.apple.com/documentation/swift/true), no error is returned if a cycle is detected for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/cancycle)*