# discriminator

**Framework**: CKTool JS  
**Kind**: property

The object’s type identifier.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute string discriminator;
```

#### Discussion

For an object that’s part of a hierarchy, an object deserializer uses a discriminator value to determine what the JSON should be deserialized as. The deserializer function emits this error if the discriminator is unrecognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/valuetypenotrecognizederror/discriminator)*