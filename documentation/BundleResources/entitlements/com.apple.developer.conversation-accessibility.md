# com.apple.developer.conversation-accessibility

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app can provide live assistance services, such as sign language interpreting or captioning, during FaceTime calls.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Details

- **Name**: `com.apple.developer.conversation-accessibility`
- **Type**: boolean



**Default**: `NO`

#### Discussion

Add this entitlement to both your container app and your app extension that conforms to [`LiveAssistanceExtension`](../../LiveCommunicationKit/liveassistanceextension.md). The container app needs the entitlement in order to call [`returnToCall(requestID:)`](../../LiveCommunicationKit/liveassistance/returntocall%28requestid%29.md).

## See Also

### LiveCommunicationKit
- [Default Calling App](./com.apple.developer.calling-app.md)
  A Boolean value that indicates whether an app can be the default calling app on someone’s device.
- [Default Dialer App](./com.apple.developer.dialing-app.md)
  A Boolean value that indicates whether an app can be the default dialer app on someone’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.conversation-accessibility)*