# setTypedPayload(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes the specified payload into the user activity’s user info dictionary.

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
func setTypedPayload<T>(_ payload: T) throws where T : Decodable, T : Encodable
```

## Discussion

> ❗ **Important**:  This method applies only to SwiftUI apps.

Use this method to set the user activity’s [`userInfo`](./userinfo.md) dictionary in a type-safe manner. After you set the [`userInfo`](./userinfo.md) dictionary using this approach, the keys in the [`userInfo`](./userinfo.md) dictionary match the coding keys from the [`Codable`](../../Swift/codable.md) type you provide as the `payload`.

If the type can’t be encoded into the [`userInfo`](./userinfo.md) dictionary, this method throws [`NSUserActivity.TypedPayloadError.encodingError`](./typedpayloaderror/encodingerror.md).

## Parameters

- `payload`: The instance to convert to [`userInfo`](./userinfo.md). The type of the `payload` instance must conform to [`Codable`](../../Swift/codable.md).

## See Also

### Managing type-safe access to user info
- [func typedPayload<T>(T.Type) throws -> T](./typedpayload%28_%29.md)
  Decodes the user activity’s user info dictionary as an instance of the specified type.
- [NSUserActivity.TypedPayloadError](./typedpayloaderror.md)
  An enumeration that describes the error types for getting and setting a typed payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/settypedpayload(_:))*