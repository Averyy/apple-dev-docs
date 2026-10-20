# init(from:)

**Framework**: Assignables  
**Kind**: init  
**Role**: Initializer

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

### Creating a user identity
- [init<T>(T)](./init%28_%29.md)
  Initializes this type eraser with a user identity to wrap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anyuseridentity/init(from:))*