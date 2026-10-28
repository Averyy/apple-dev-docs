# SecTranformCustomGetAttribute

**Framework**: Security  
**Kind**: func  
**Role**: Function

Gets an attribute value from a custom transform.

**Availability**:
- macOS 10.7+ - Deprecated in 10.8

> **Deprecated**: Use [`SecTransformCustomGetAttribute(_:_:_:)`](./sectransformcustomgetattribute%28_,_,_%29.md) instead.

## Declaration

```c
extern CFTypeRefSecTranformCustomGetAttribute(SecTransformImplementationRef ref, SecTransformStringOrAttributeRef attribute, SecTransformMetaAttributeType type);
```

## Return Value

The value of the attribute.

## Discussion

> ❗ **Important**:  This function is deprecated. Use [`SecTransformCustomGetAttribute(_:_:_:)`](./sectransformcustomgetattribute%28_,_,_%29.md) instead.

## Parameters

- `ref`: A [`SecTransformImplementationRef`](./sectransformimplementationref.md) that is bound to an instance of a custom transform.
- `attribute`: The name or the attribute handle of the attribute whose value is to be retrieved. When using a name, see [Transform Attributes](./transform-attributes.md) for a list of valid key names.
- `type`: The type of data to be retrieved for the attribute. See the discussion on [`SecTransformMetaAttributeType`](./sectransformmetaattributetype.md) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectranformcustomgetattribute)*