# init(from:)

**Framework**: LightweightCodeRequirements  
**Kind**: init

Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int64`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset/init(from:))*