# SecTransformMetaAttributeType.required

**Framework**: Security  
**Kind**: case  
**Role**: Case

Indicates whether the attribute value is optional.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
case required
```

```c
kSecTransformMetaAttributeRequired
```

#### Discussion

Specifies if an attribute must have a non `NULL` value set or have an incoming connection before the transform starts to execute. This metadata has a default value of [`true`](../../Swift/true.md) for the input attribute, but [`false`](../../Swift/false.md) for all other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/required)*