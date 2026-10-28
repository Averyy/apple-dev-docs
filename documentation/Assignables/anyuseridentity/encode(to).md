# encode(to:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method

Encodes this value into the given encoder.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

## Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

### Instance Methods
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/anyuseridentity/encode(to:))*