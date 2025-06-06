# encode(to:)

**Framework**: System  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [init(from: any Decoder) throws](filedescriptor/accessmode/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/accessmode/encode(to:))*