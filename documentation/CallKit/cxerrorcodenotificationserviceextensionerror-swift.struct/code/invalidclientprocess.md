# CXErrorCodeNotificationServiceExtensionError.Code.invalidClientProcess

**Framework**: CallKit  
**Kind**: case  
**Role**: Case

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

```c
CXErrorCodeNotificationServiceExtensionErrorInvalidClientProcess
```

#### Discussion

Only call the [`reportNewIncomingVoIPPushPayload(_:completion:)`](../../cxprovider/reportnewincomingvoippushpayload%28_,completion%29.md) method from a [`UNNotificationServiceExtension`](../../../UserNotifications/unnotificationserviceextension.md) object that is responding to an incoming notification request.

## See Also

### Error Codes
- [CXErrorCodeNotificationServiceExtensionError.Code.missingNotificationFilteringEntitlement](./missingnotificationfilteringentitlement.md)
  An error indicating that the notification service extension is missing the required filtering entitlement.
- [CXErrorCodeNotificationServiceExtensionError.Code.unknown](./unknown.md)
  An error that occurs when there is an unknown problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxerrorcodenotificationserviceextensionerror-swift.struct/code/invalidclientprocess)*