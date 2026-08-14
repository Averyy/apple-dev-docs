# SecTransformMetaAttributeType.required

**Framework**: Security  
**Kind**: case

Indicates whether the attribute value is optional.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case required
```

#### Discussion

Specifies if an attribute must have a non `NULL` value set or have an incoming connection before the transform starts to execute. This metadata has a default value of [`true`](https://developer.apple.com/documentation/swift/true) for the input attribute, but [`false`](https://developer.apple.com/documentation/swift/false) for all other attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformmetaattributetype/required)*