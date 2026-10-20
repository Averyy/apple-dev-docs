# CXErrorCodeNotificationServiceExtensionError.Code

**Framework**: CallKit  
**Kind**: enum  
**Role**: Enumeration

Constants for errors returned when reporting new, incoming VoIP calls.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum CXErrorCodeNotificationServiceExtensionError : NSInteger;
```

## Topics

### Error Codes
- [CXErrorCodeNotificationServiceExtensionError.Code.invalidClientProcess](./code/invalidclientprocess.md)
  An error indicating that an invalid client process reported the incoming call.
- [CXErrorCodeNotificationServiceExtensionError.Code.missingNotificationFilteringEntitlement](./code/missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [CXErrorCodeNotificationServiceExtensionError.Code.unknown](./code/unknown.md)
  An error that occurs when there is an unknown problem.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/code)*