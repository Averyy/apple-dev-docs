# encode(_:to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func encode(_ value: Self.Value, to encoder: any Encoder) throws
```

Available when `Value` conforms to `Encodable`.

#### Discussion

The default implementation calls down to the value’s [`encode(to:)`](../../Swift/encodable/encode%28to%29.md) method.

This method throws an error if writing the encoder fails.

## Parameters

- `value`: The value to encode.
- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodableattributedstringkey/encode(_:to:)-47oas)*