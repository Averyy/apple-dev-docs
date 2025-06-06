# SecTransformCustomSetAttribute(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Sets an attribute value on a custom transform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformCustomSetAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ type: SecTransformMetaAttributeType, _ value: CFTypeRef?) -> CFTypeRef?
```

#### Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the error’s memory when you are done with it.

#### Discussion

Unlike the [`SecTransformSetAttribute(_:_:_:_:)`](sectransformsetattribute(_:_:_:_:).md) function this function can set attribute values while a transform is executing. These values are limited to the custom transform instance that is bound to the `ref` parameter.

## Parameters

- `ref`: A   that is bound to an instance of a custom transform.
- `attribute`: The name or the attribute handle of the attribute whose value is to be set. When using a name, see   for a list of valid key names.
- `type`: The type of data to be retrieved for the attribute. See the discussion on   for details.
- `value`: The new value for the attribute


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformcustomsetattribute(_:_:_:_:))*