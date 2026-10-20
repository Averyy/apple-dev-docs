# init(_:)

**Framework**: Assignables  
**Kind**: init  
**Role**: Initializer

Initializes this type eraser with a user identity to wrap.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
init<T>(_ userIdentity: T) where T : UserIdentity
```

## See Also

### Creating a user identity
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anyuseridentity/init(_:))*