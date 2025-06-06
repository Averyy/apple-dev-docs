# CXErrorCodeNotificationServiceExtensionError.Code.missingNotificationFilteringEntitlement

**Framework**: CallKit  
**Kind**: case

An error indicating that the notification service extension is missing the required filtering entitlement.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case missingNotificationFilteringEntitlement
```

#### Discussion

To call the [`reportNewIncomingVoIPPushPayload(_:completion:)`](cxprovider/reportnewincomingvoippushpayload(_:completion:).md) method, a notification service extension must have a `com.apple.developer.usernotifications.filtering` entitlement. To apply for this entitlement, see [`https://developer.apple.com/contact/request/notification-service`](https://developer.apple.comhttps://developer.apple.com/contact/request/notification-service).

After you receive permission to use the entitlement, add [`com.apple.developer.usernotifications.filtering`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.usernotifications.filtering) to the entitlements file for the Notification Service Extension target.

## See Also

- [CXErrorCodeNotificationServiceExtensionError.Code.invalidClientProcess](cxerrorcodenotificationserviceextensionerror-swift.struct/code/invalidclientprocess.md)
  An error indicating that an invalid client process reported the incoming call.
- [CXErrorCodeNotificationServiceExtensionError.Code.unknown](cxerrorcodenotificationserviceextensionerror-swift.struct/code/unknown.md)
  An error that occurs when there is an unknown problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/code/missingnotificationfilteringentitlement)*