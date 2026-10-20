# NSUserActivity.TypedPayloadError

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

Use this enumeration to manage errors from [`typedPayload(_:)`](./typedpayload%28_%29.md) and [`setTypedPayload(_:)`](./settypedpayload%28_%29.md).

## Topics

### Typed payload errors
- [NSUserActivity.TypedPayloadError.encodingError](./typedpayloaderror/encodingerror.md)
  An encoding error that indicates that the content failed to encode into a valid dictionary.
- [NSUserActivity.TypedPayloadError.invalidContent](./typedpayloaderror/invalidcontent.md)
  A decoding error that indicates that the user info dictionary is empty or invalid.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing type-safe access to user info
- [func setTypedPayload<T>(T) throws](./settypedpayload%28_%29.md)
  Encodes the specified payload into the user activity’s user info dictionary.
- [func typedPayload<T>(T.Type) throws -> T](./typedpayload%28_%29.md)
  Decodes the user activity’s user info dictionary as an instance of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/typedpayloaderror)*