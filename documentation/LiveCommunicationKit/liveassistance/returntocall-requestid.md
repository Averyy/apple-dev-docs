# returnToCall(requestID:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Requests that framework return to the FaceTime call, in order to resume the live assistance request.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
static func returnToCall(requestID: UUID)
```

#### Discussion

Use this method when the framework launches your app in order to satisfy a request from your extension for the person using the app to sign in or provide other information. After your app collects the needed information, call this method from inside the [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/swiftui/view/oncontinueuseractivity(_:perform:)) (SwiftUI) or [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:continue:restorationhandler:)) (UIKit) method where you handle the activity type [`containerAppLaunchActivityType`](liveassistance/containerapplaunchactivitytype.md). For the parameter `requestID`, fetch the value of [`containerAppLaunchRequestIDKey`](liveassistance/containerapplaunchrequestidkey.md) from the [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo) dictionary of the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) sent to the launch method.

This method returns immediately. After you call it, the system foregrounds the FaceTime call and invokes the extension’s [`resumeRequest(_:)`](liveassistanceextension/resumerequest(_:).md) to indicate that the container app has finished its work and the extension can continue setting up live assistance.

If the system doesn’t recognize `requestID` — possibly because the call ended or the person canceled the request — the framework silently ignores `returnToCall(_:)`. The container app doesn’t need to perform any clean-up work in this situation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/returntocall(requestid:))*