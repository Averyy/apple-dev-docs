# init(from:)

**Framework**: System  
**Kind**: init

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.

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
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](filedescriptor/openoptions/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/init(from:))*