# encode(_:to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Encodes an Objective-C value to the provided encoder, using a default implementation.

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

Available when `Value` inherits `NSObject` and `Value` conforms to `NSSecureCoding`.

#### Discussion

The default implementation uses an [`NSKeyedArchiver`](../nskeyedarchiver.md) on the object, then calls [`encode(to:)`](../../Swift/encodable/encode%28to%29.md) on the resulting data.

This method throws an error if writing to the encoder fails.

## Parameters

- `value`: The value to encode.
- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/encodableattributedstringkey/encode(_:to:)-16dss)*