# com.apple.developer.conversation-accessibility

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app can provide live assistance services, such as sign language interpreting or captioning, during FaceTime calls.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)



**Type**: boolean

**Default**: `NO`

#### Discussion

Add this entitlement to both your container app and your app extension that conforms to [`LiveAssistanceExtension`](https://developer.apple.com/documentation/livecommunicationkit/liveassistanceextension). The container app needs the entitlement in order to call [`returnToCall(requestID:)`](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/returntocall(requestid:)).

## See Also

- [Default Calling App](entitlements/com.apple.developer.calling-app.md)
  A Boolean value that indicates whether an app can be the default calling app on someone’s device.
- [Default Dialer App](entitlements/com.apple.developer.dialing-app.md)
  A Boolean value that indicates whether an app can be the default dialer app on someone’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.conversation-accessibility)*