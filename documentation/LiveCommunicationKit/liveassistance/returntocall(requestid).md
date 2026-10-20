# returnToCall(requestID:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Type Method

Requests that framework return to the FaceTime call, in order to resume the live assistance request.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+

## Declaration

```swift
@MainActor
static func returnToCall(requestID: UUID)
```

#### Discussion

Use this method when the framework launches your app in order to satisfy a request from your extension for the person using the app to sign in or provide other information. After your app collects the needed information, call this method from inside the [`onContinueUserActivity(_:perform:)`](../../SwiftUI/view/oncontinueuseractivity%28_,perform%29.md) (SwiftUI) or [`application(_:continue:restorationHandler:)`](../../UIKit/uiapplicationdelegate/application%28_,continue,restorationhandler%29.md) (UIKit) method where you handle the activity type [`containerAppLaunchActivityType`](./containerapplaunchactivitytype.md). For the parameter `requestID`, fetch the value of [`containerAppLaunchRequestIDKey`](./containerapplaunchrequestidkey.md) from the [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) sent to the launch method.

This method returns immediately. After you call it, the system foregrounds the FaceTime call and invokes the extension’s [`resumeRequest(_:)`](../liveassistanceextension/resumerequest%28_%29.md) to indicate that the container app has finished its work and the extension can continue setting up live assistance.

If the system doesn’t recognize `requestID` — possibly because the call ended or the person canceled the request — the framework silently ignores `returnToCall(_:)`. The container app doesn’t need to perform any clean-up work in this situation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance/returntocall(requestid:))*