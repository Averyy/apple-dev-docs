# SecTransformCustomGetAttribute(_:_:_:)

**Framework**: Security  
**Kind**: func

Gets an attribute value from a custom transform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCustomGetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType) -> CFTypeRef?
```

#### Return Value

The value of the attribute.

## Parameters

- `ref`: A   that is bound to an instance of a custom transform.
- `attribute`: The name or the attribute handle of the attribute whose value is to be retrieved. When using a name, see   for a list of valid key names.
- `type`: The type of data to be retrieved for the attribute. See the discussion on   for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcustomgetattribute(_:_:_:))*