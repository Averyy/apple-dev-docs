# CXErrorCodeNotificationServiceExtensionError.Code

**Framework**: CallKit  
**Kind**: enum

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

## Topics

### Error Codes
- [CXErrorCodeNotificationServiceExtensionError.Code.invalidClientProcess](cxerrorcodenotificationserviceextensionerror-swift.struct/code/invalidclientprocess.md)
  An error indicating that an invalid client process reported the incoming call.
- [CXErrorCodeNotificationServiceExtensionError.Code.missingNotificationFilteringEntitlement](cxerrorcodenotificationserviceextensionerror-swift.struct/code/missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [CXErrorCodeNotificationServiceExtensionError.Code.unknown](cxerrorcodenotificationserviceextensionerror-swift.struct/code/unknown.md)
  An error that occurs when there is an unknown problem.
### Initializers
- [init?(rawValue: Int)](cxerrorcodenotificationserviceextensionerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/code)*