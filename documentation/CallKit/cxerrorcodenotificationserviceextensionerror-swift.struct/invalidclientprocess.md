# invalidClientProcess

**Framework**: CallKit  
**Kind**: property

An error indicating that an invalid client process reported the incoming call.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var invalidClientProcess: CXErrorCodeNotificationServiceExtensionError.Code { get }
```

#### Discussion

Only call the [`reportNewIncomingVoIPPushPayload(_:completion:)`](cxprovider/reportnewincomingvoippushpayload(_:completion:).md) method from a [`UNNotificationServiceExtension`](https://developer.apple.com/documentation/UserNotifications/UNNotificationServiceExtension) object that is responding to an incoming notification request.

## See Also

- [static var missingNotificationFilteringEntitlement: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [static var unknown: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/unknown.md)
  An error that occurs when there is an unknown problem.
- [CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/code.md)
  Constants for errors returned when reporting new, incoming VoIP calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/invalidclientprocess)*