# NSUserActivity.TypedPayloadError

**Framework**: Foundation  
**Kind**: enum

An enumeration that describes the error types for getting and setting a typed payload.

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
enum TypedPayloadError
```

#### Overview

Use this enumeration to manage errors from [`typedPayload(_:)`](nsuseractivity/typedpayload(_:).md) and [`setTypedPayload(_:)`](nsuseractivity/settypedpayload(_:).md).

## Topics

### Typed payload errors
- [NSUserActivity.TypedPayloadError.encodingError](nsuseractivity/typedpayloaderror/encodingerror.md)
  An encoding error that indicates that the content failed to encode into a valid dictionary.
- [NSUserActivity.TypedPayloadError.invalidContent](nsuseractivity/typedpayloaderror/invalidcontent.md)
  A decoding error that indicates that the user info dictionary is empty or invalid.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setTypedPayload<T>(T) throws](nsuseractivity/settypedpayload(_:).md)
  Encodes the specified payload into the user activity’s user info dictionary.
- [func typedPayload<T>(T.Type) throws -> T](nsuseractivity/typedpayload(_:).md)
  Decodes the user activity’s user info dictionary as an instance of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayloaderror)*