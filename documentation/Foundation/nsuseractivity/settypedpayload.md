# setTypedPayload(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

> ❗ **Important**:  This method applies only to SwiftUI apps.

 This method applies only to SwiftUI apps.

Use this method to set the user activity’s [`userInfo`](nsuseractivity/userinfo.md) dictionary in a type-safe manner. After you set the [`userInfo`](nsuseractivity/userinfo.md) dictionary using this approach, the keys in the [`userInfo`](nsuseractivity/userinfo.md) dictionary match the coding keys from the [`Codable`](https://developer.apple.com/documentation/Swift/Codable) type you provide as the `payload`.

If the type can’t be encoded into the [`userInfo`](nsuseractivity/userinfo.md) dictionary, this method throws [`NSUserActivity.TypedPayloadError.encodingError`](nsuseractivity/typedpayloaderror/encodingerror.md).

## Parameters

- `payload`: The instance to convert to  . The type of the   instance must conform to  .

## See Also

- [func typedPayload<T>(T.Type) throws -> T](nsuseractivity/typedpayload(_:).md)
  Decodes the user activity’s user info dictionary as an instance of the specified type.
- [NSUserActivity.TypedPayloadError](nsuseractivity/typedpayloaderror.md)
  An enumeration that describes the error types for getting and setting a typed payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/settypedpayload(_:))*