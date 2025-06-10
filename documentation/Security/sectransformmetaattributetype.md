# SecTransformMetaAttributeType

**Framework**: Security  
**Kind**: enum

The keys that describe the metadata attributes of transform attributes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum SecTransformMetaAttributeType
```

#### Overview

Use one of these values as the `type` parameter in a call to the [`SecTransformCustomSetAttribute(_:_:_:_:)`](sectransformcustomsetattribute(_:_:_:_:).md) or [`SecTransformCustomGetAttribute(_:_:_:)`](sectransformcustomgetattribute(_:_:_:).md) function. These values allow you to access not only the value of an attribute, as you would do directly with calls the [`SecTransformSetAttribute(_:_:_:_:)`](sectransformsetattribute(_:_:_:_:).md) or [`SecTransformGetAttribute(_:_:)`](sectransformgetattribute(_:_:).md) function, but also the metadata associated with that attribute, such as the name of an attribute, or whether it is required to have a value.

## Topics

### Constants
- [SecTransformMetaAttributeType.canCycle](sectransformmetaattributetype/cancycle.md)
  The transform allows cyclic behavior.
- [SecTransformMetaAttributeType.deferred](sectransformmetaattributetype/deferred.md)
  The attribute defers notifications.
- [SecTransformMetaAttributeType.externalize](sectransformmetaattributetype/externalize.md)
  The attribute is exportable.
- [SecTransformMetaAttributeType.hasInboundConnection](sectransformmetaattributetype/hasinboundconnection.md)
  The attribute has an inbound connection.
- [SecTransformMetaAttributeType.hasOutboundConnections](sectransformmetaattributetype/hasoutboundconnections.md)
  The attribute has an outbound connection.
- [SecTransformMetaAttributeType.name](sectransformmetaattributetype/name.md)
  The name of the attribute.
- [SecTransformMetaAttributeType.ref](sectransformmetaattributetype/ref.md)
  A direct reference to an attribute’s value.
- [SecTransformMetaAttributeType.required](sectransformmetaattributetype/required.md)
  Indicates whether the attribute value is optional.
- [SecTransformMetaAttributeType.requiresOutboundConnection](sectransformmetaattributetype/requiresoutboundconnection.md)
  The attribute requires an outbound connection.
- [SecTransformMetaAttributeType.stream](sectransformmetaattributetype/stream.md)
  The attribute expects stream operation.
- [SecTransformMetaAttributeType.value](sectransformmetaattributetype/value.md)
  The actual value of the attribute.
### Initializers
- [init?(rawValue: CFIndex)](sectransformmetaattributetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype)*