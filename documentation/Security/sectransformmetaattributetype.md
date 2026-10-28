# SecTransformMetaAttributeType

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The keys that describe the metadata attributes of transform attributes.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
enum SecTransformMetaAttributeType
```

```c
enum SecTransformMetaAttributeType : CFIndex;
```

## Overview

Use one of these values as the `type` parameter in a call to the [`SecTransformCustomSetAttribute(_:_:_:_:)`](./sectransformcustomsetattribute%28_,_,_,_%29.md) or [`SecTransformCustomGetAttribute(_:_:_:)`](./sectransformcustomgetattribute%28_,_,_%29.md) function. These values allow you to access not only the value of an attribute, as you would do directly with calls the [`SecTransformSetAttribute(_:_:_:_:)`](./sectransformsetattribute%28_,_,_,_%29.md) or [`SecTransformGetAttribute(_:_:)`](./sectransformgetattribute%28_,_%29.md) function, but also the metadata associated with that attribute, such as the name of an attribute, or whether it is required to have a value.

## Topics

### Constants
- [SecTransformMetaAttributeType.canCycle](./sectransformmetaattributetype/cancycle.md)
  The transform allows cyclic behavior.
- [SecTransformMetaAttributeType.deferred](./sectransformmetaattributetype/deferred.md)
  The attribute defers notifications.
- [SecTransformMetaAttributeType.externalize](./sectransformmetaattributetype/externalize.md)
  The attribute is exportable.
- [SecTransformMetaAttributeType.hasInboundConnection](./sectransformmetaattributetype/hasinboundconnection.md)
  The attribute has an inbound connection.
- [SecTransformMetaAttributeType.hasOutboundConnections](./sectransformmetaattributetype/hasoutboundconnections.md)
  The attribute has an outbound connection.
- [SecTransformMetaAttributeType.name](./sectransformmetaattributetype/name.md)
  The name of the attribute.
- [SecTransformMetaAttributeType.ref](./sectransformmetaattributetype/ref.md)
  A direct reference to an attribute’s value.
- [SecTransformMetaAttributeType.required](./sectransformmetaattributetype/required.md)
  Indicates whether the attribute value is optional.
- [SecTransformMetaAttributeType.requiresOutboundConnection](./sectransformmetaattributetype/requiresoutboundconnection.md)
  The attribute requires an outbound connection.
- [SecTransformMetaAttributeType.stream](./sectransformmetaattributetype/stream.md)
  The attribute expects stream operation.
- [SecTransformMetaAttributeType.value](./sectransformmetaattributetype/value.md)
  The actual value of the attribute.
### Initializers
- [init?(rawValue: CFIndex)](./sectransformmetaattributetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype)*