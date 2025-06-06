# SecTransformGetAttribute(_:_:)

**Framework**: Security  
**Kind**: func

Gets the current value of a transform attribute.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformGetAttribute(_ transformRef: SecTransform, _ key: CFString) -> CFTypeRef?
```

#### Return Value

The value of an attribute. If this attribute is being set as the output of another transform and [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md) has not been called on the transform or if the attribute does not exists then `NULL` will be returned.

#### Discussion

This may be called after [`SecTransformExecute(_:_:)`](sectransformexecute(_:_:).md).

## Parameters

- `transformRef`: The transform whose attribute value will be retrieved.
- `key`: The name of the attribute to retrieve. See    for a list of valid keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformgetattribute(_:_:))*