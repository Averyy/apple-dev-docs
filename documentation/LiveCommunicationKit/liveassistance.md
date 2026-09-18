# LiveAssistance

**Framework**: LiveCommunicationKit  
**Kind**: enum

A namespace to collect APIs for use by container apps that provide live assistance services.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)
- Mac Catalyst 27.1+ (Beta)
- macOS 27.1+
- visionOS 27.1+

## Declaration

```swift
enum LiveAssistance
```

#### Overview

To provide interpreter, captioning, or other services that work with FaceTime calls, create a container app that uses the [`LiveAssistance`](liveassistance.md) APIs, as well as an app extension that conforms to the [`LiveAssistanceExtension`](liveassistanceextension.md) protocol.

When a participant in a FaceTime calls wants to use live assistance services, they primarily interact with the app extension. If the extension needs further information to set up the service, it launches the app by returning [`LiveAssistanceRequest.Response.requiresUserInput(reason:)`](liveassistancerequest/response/requiresuserinput(reason:).md) to the request from the framework. This response causes the system to launch the container app, which uses the APIs in this type.

##### Handling App Launch

To prepare your container app, start by adding `com.apple.conversation-accessibility.container-app-launch` to the `NSUserActivityTypes` in your app’s information property list. This allows the framework to launch your app when the extension needs the person using the app to sign in or provide other information.

The framework launches your app with [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/swiftui/view/oncontinueuseractivity(_:perform:)) (SwiftUI) or [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:continue:restorationhandler:)) (UIKit). Inspect the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) to verify that the activity type is [`containerAppLaunchActivityType`](liveassistance/containerapplaunchactivitytype.md). If so, retrieve the launch reason and the request identifier from the [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/userinfo). The launch reason indicates whether the extension needs the app to authenticate the person requesting the service, or if they need to perform some other configuration or approval. Once your app resolves that, you use the request identifier and call [`returnToCall(requestID:)`](liveassistance/returntocall(requestid:).md) to resume or relaunch the extension and continue setting up the live assistance service.

The following example shows how a SwiftUI container app would handle being launched in response to a request from its app extension. It retrieves the request identifier and launch reason from the [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity), and then calls an asynchronous `myHandleAccessibilityLaunch(requestID:reason:)` method to handle any needed login or configuration and then resume the request.

```swift
var body: some Scene {
    WindowGroup {
        ContentView()
            .onContinueUserActivity(LiveAssistance.containerAppLaunchActivityType) { activity in
                guard
                    let requestID = activity.userInfo?[LiveAssistance.containerAppLaunchRequestIDKey] as? /// UUID,
                    let rawReason = activity.userInfo?[LiveAssistance.containerAppLaunchReasonKey] as? /// String,
                    let reason = LiveAssistanceLaunchReason(rawValue: rawReason)
                else { return }
                Task { await myHandleAccessibilityLaunch(requestID: requestID, reason: reason) }
            }
    }
}
```

## Topics

### Identifying the app extension
- [static let extensionPointName: String](liveassistance/extensionpointname.md)
  The extension point identifier.
### Responding to a container app launch
- [static let containerAppLaunchActivityType: String](liveassistance/containerapplaunchactivitytype.md)
  The user activity type sent to the container app.
- [static let containerAppLaunchRequestIDKey: String](liveassistance/containerapplaunchrequestidkey.md)
  A key the container app uses to retrieve a unique identifier for the live assistance request.
- [static let containerAppLaunchReasonKey: String](liveassistance/containerapplaunchreasonkey.md)
  A key the container app uses to retrieve the reason the app extension requested the framework to launch the container app.
- [enum LiveAssistanceLaunchReason](liveassistancelaunchreason.md)
  A type that indicates why the live assistance extension needs to launch its container app.
### Returning to a call
- [static func returnToCall(requestID: UUID)](liveassistance/returntocall(requestid:).md)
  Requests that framework return to the FaceTime call, in order to resume the live assistance request.

## See Also

- [protocol LiveAssistanceExtension](liveassistanceextension.md)
  The protocol you extend to provide live assistance services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/liveassistance)*