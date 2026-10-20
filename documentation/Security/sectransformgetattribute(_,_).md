# SecTransformGetAttribute(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Gets the current value of a transform attribute.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformGetAttribute(_ transformRef: SecTransform, _ key: CFString) -> CFTypeRef?
```

```c
extern CFTypeRefSecTransformGetAttribute(SecTransformRef transformRef, CFStringRef key);
```

#### Return Value

The value of an attribute. If this attribute is being set as the output of another transform and [`SecTransformExecute(_:_:)`](./sectransformexecute%28_,_%29.md) has not been called on the transform or if the attribute does not exists then `NULL` will be returned.

#### Discussion

This may be called after [`SecTransformExecute(_:_:)`](./sectransformexecute%28_,_%29.md).

## Parameters

- `transformRef`: The transform whose attribute value will be retrieved.
- `key`: The name of the attribute to retrieve. See [Transform Attributes](./transform-attributes.md)  for a list of valid keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformgetattribute(_:_:))*