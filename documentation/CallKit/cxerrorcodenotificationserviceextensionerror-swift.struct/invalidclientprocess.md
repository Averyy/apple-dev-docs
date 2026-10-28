# invalidClientProcess

**Framework**: CallKit  
**Kind**: property  
**Role**: Type Property

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

## Discussion

Only call the [`reportNewIncomingVoIPPushPayload(_:completion:)`](../cxprovider/reportnewincomingvoippushpayload%28_,completion%29.md) method from a [`UNNotificationServiceExtension`](../../UserNotifications/unnotificationserviceextension.md) object that is responding to an incoming notification request.

## See Also

### Understanding Error Codes
- [static var missingNotificationFilteringEntitlement: CXErrorCodeNotificationServiceExtensionError.Code](./missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [static var unknown: CXErrorCodeNotificationServiceExtensionError.Code](./unknown.md)
  An error that occurs when there is an unknown problem.
- [CXErrorCodeNotificationServiceExtensionError.Code](./code.md)
  Constants for errors returned when reporting new, incoming VoIP calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/invalidclientprocess)*