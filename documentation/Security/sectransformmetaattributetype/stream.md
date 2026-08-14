# SecTransformMetaAttributeType.stream

**Framework**: Security  
**Kind**: case

The attribute expects stream operation.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case stream
```

#### Discussion

Specifies if the attribute should expect a series of values ending with a `NULL` to specify the end of the data stream. This metadata has a default value of [`true`](https://developer.apple.com/documentation/swift/true) for the input and output attributes, but is [`false`](https://developer.apple.com/documentation/swift/false) for all other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/stream)*