# SecTransformMetaAttributeType.canCycle

**Framework**: Security  
**Kind**: case  
**Role**: Case

The transform allows cyclic behavior.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
case canCycle
```

```c
kSecTransformMetaAttributeCanCycle
```

#### Discussion

A transform group is a directed graph which is typically acyclic. Some transforms need to work with cycles. For example, a transform that emits a header and trailer around the data of another transform must create a cycle. If this metadata set to [`true`](../../Swift/true.md), no error is returned if a cycle is detected for this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/cancycle)*