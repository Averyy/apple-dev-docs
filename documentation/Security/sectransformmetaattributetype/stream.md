# SecTransformMetaAttributeType.stream

**Framework**: Security  
**Kind**: case  
**Role**: Case

The attribute expects stream operation.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
case stream
```

```c
kSecTransformMetaAttributeStream
```

#### Discussion

Specifies if the attribute should expect a series of values ending with a `NULL` to specify the end of the data stream. This metadata has a default value of [`true`](../../Swift/true.md) for the input and output attributes, but is [`false`](../../Swift/false.md) for all other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/stream)*