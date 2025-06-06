# SecTransformAttributeActionBlock

**Framework**: Security  
**Kind**: typealias

A block used to override the default attribute handling for when an attribute is set.

**Availability**:
- macOS 10.7+

## Declaration

```swift
typealias SecTransformAttributeActionBlock = (SecTransformAttribute, CFTypeRef) -> Unmanaged<CFTypeRef>?
```

#### Return Value

The new value of the attribute if successful or a doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 object on failure. If a transform needs to have a doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 as the value of an attribute, then place the object in a container, such as a [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) or [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) object.

## Parameters

- `attribute`: The attribute whose default is being overridden or NULL if this is a generic notification override
- `value`: Proposed new value for the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformattributeactionblock)*