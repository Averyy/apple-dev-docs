# typedPayload(_:)

**Framework**: Foundation  
**Kind**: method

Decodes the user activity’s user info dictionary as an instance of the specified type.

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
func typedPayload<T>(_ type: T.Type) throws -> T where T : Decodable, T : Encodable
```

#### Return Value

The type-safe instance.

#### Discussion

> ❗ **Important**:  This method applies only to SwiftUI apps.

 This method applies only to SwiftUI apps.

Use this method to retrieve information from the user activity’s [`userInfo`](nsuseractivity/userinfo.md) dictionary in a type-safe manner.

If the type can’t be decoded from the [`userInfo`](nsuseractivity/userinfo.md) dictionary, this method throws [`NSUserActivity.TypedPayloadError.invalidContent`](nsuseractivity/typedpayloaderror/invalidcontent.md).

## Parameters

- `type`: The type to decode from  . The   must conform to  .

## See Also

- [func setTypedPayload<T>(T) throws](nsuseractivity/settypedpayload(_:).md)
  Encodes the specified payload into the user activity’s user info dictionary.
- [NSUserActivity.TypedPayloadError](nsuseractivity/typedpayloaderror.md)
  An enumeration that describes the error types for getting and setting a typed payload.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayload(_:))*