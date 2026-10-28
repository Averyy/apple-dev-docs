# SecTransformAttributeActionBlock

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A block used to override the default attribute handling for when an attribute is set.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
typealias SecTransformAttributeActionBlock = (SecTransformAttribute, CFTypeRef) -> Unmanaged<CFTypeRef>?
```

```c
typedef const void *(^)(const void *, const void *) SecTransformAttributeActionBlock;
```

## Return Value

The new value of the attribute if successful or a [`CFError`](../CoreFoundation/cferror.md) object on failure. If a transform needs to have a [`CFError`](../CoreFoundation/cferror.md) as the value of an attribute, then place the object in a container, such as a [`CFArray`](../CoreFoundation/cfarray.md) or [`CFDictionary`](../CoreFoundation/cfdictionary.md) object.

## Parameters

- `attribute`: The attribute whose default is being overridden or NULL if this is a generic notification override
- `value`: Proposed new value for the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformattributeactionblock)*