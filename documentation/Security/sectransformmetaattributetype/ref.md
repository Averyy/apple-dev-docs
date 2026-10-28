# SecTransformMetaAttributeType.ref

**Framework**: Security  
**Kind**: case  
**Role**: Case

A direct reference to an attribute’s value.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
case ref
```

```c
kSecTransformMetaAttributeRef
```

## Discussion

This reference allows for direct access to an attribute without having to look up the attribute by name. If a transform commonly uses an attribute, using a reference speeds up the use of that attribute. Attribute references are not visible or valid from outside of the particular transform instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ref)*