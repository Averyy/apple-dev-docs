# CXErrorCodeNotificationServiceExtensionError.Code.invalidClientProcess

**Framework**: CallKit  
**Kind**: case

An error indicating that an invalid client process reported the incoming call.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case invalidClientProcess
```

#### Discussion

Only call the [`reportNewIncomingVoIPPushPayload(_:completion:)`](cxprovider/reportnewincomingvoippushpayload(_:completion:).md) method from a [`UNNotificationServiceExtension`](https://developer.apple.com/documentation/UserNotifications/UNNotificationServiceExtension) object that is responding to an incoming notification request.

## See Also

- [CXErrorCodeNotificationServiceExtensionError.Code.missingNotificationFilteringEntitlement](cxerrorcodenotificationserviceextensionerror-swift.struct/code/missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [CXErrorCodeNotificationServiceExtensionError.Code.unknown](cxerrorcodenotificationserviceextensionerror-swift.struct/code/unknown.md)
  An error that occurs when there is an unknown problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/code/invalidclientprocess)*