# missingNotificationFilteringEntitlement

**Framework**: CallKit  
**Kind**: property

An error indicating that the notification service extension is missing the required filtering entitlement.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var missingNotificationFilteringEntitlement: CXErrorCodeNotificationServiceExtensionError.Code { get }
```

#### Discussion

To call the [`reportNewIncomingVoIPPushPayload(_:completion:)`](cxprovider/reportnewincomingvoippushpayload(_:completion:).md) method, a notification service extension must have a `com.apple.developer.usernotifications.filtering` entitlement. To apply for this entitlement, see [`https://developer.apple.com/contact/request/notification-service`](https://developer.apple.comhttps://developer.apple.com/contact/request/notification-service).

After you receive permission to use the entitlement, add [`com.apple.developer.usernotifications.filtering`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.usernotifications.filtering) to the entitlements file for the Notification Service Extension target.

## See Also

- [static var invalidClientProcess: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/invalidclientprocess.md)
  An error indicating that an invalid client process reported the incoming call.
- [static var unknown: CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/unknown.md)
  An error that occurs when there is an unknown problem.
- [CXErrorCodeNotificationServiceExtensionError.Code](cxerrorcodenotificationserviceextensionerror-swift.struct/code.md)
  Constants for errors returned when reporting new, incoming VoIP calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/missingnotificationfilteringentitlement)*