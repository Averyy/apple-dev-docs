# SecTransformCustomGetAttribute(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Gets an attribute value from a custom transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType) -> CFTypeRef?
```

```c
extern CFTypeRefSecTransformCustomGetAttribute(SecTransformImplementationRef ref, SecTransformStringOrAttributeRef attribute, SecTransformMetaAttributeType type);
```

#### Return Value

The value of the attribute.

## Parameters

- `ref`: A [`SecTransformImplementationRef`](./sectransformimplementationref.md) that is bound to an instance of a custom transform.
- `attribute`: The name or the attribute handle of the attribute whose value is to be retrieved. When using a name, see [Transform Attributes](./transform-attributes.md) for a list of valid key names.
- `type`: The type of data to be retrieved for the attribute. See the discussion on [`SecTransformMetaAttributeType`](./sectransformmetaattributetype.md) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcustomgetattribute(_:_:_:))*