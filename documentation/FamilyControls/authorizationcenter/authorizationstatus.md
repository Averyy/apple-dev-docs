# authorizationStatus

**Framework**: Family Controls  
**Kind**: property  
**Role**: Instance Property

The status of your app’s authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
@Published
<AuthorizationStatus> var authorizationStatus: AuthorizationStatus { get }
```

## Discussion

The initial value is always [`AuthorizationStatus.notDetermined`](../authorizationstatus/notdetermined.md). The system sets this property only after a call to [`requestAuthorization(for:)`](./requestauthorization%28for%29.md) succeeds. It then updates the property until a call to [`revokeAuthorization(completionHandler:)`](./revokeauthorization%28completionhandler%29.md) succeeds or your app exits.

To track changes to your app’s authorization status, attach a [`Subscriber`](../../Combine/subscriber.md) to the `authorizationStatus` property.

```swift
let cancellable = center.$authorizationStatus
.sink() {
    switch center.authorizationStatus {
    case .notDetermined:
        // Handle the change to notDetermined.
    case .denied:
        // Handle the change to denied.
    case .approved:
        // Handle the change to approved.
   }
}
```

Alternatively, you can assign the [`AuthorizationCenter`](../authorizationcenter.md) to an [`ObservedObject`](../../SwiftUI/observedobject.md) property inside a [`View`](../../SwiftUI/view.md). The system update the view whenever the status changes.

```swift
@ObservedObject var center = AuthorizationCenter.shared
```

The status may change due to external events, such as a child graduating to an adult account, or a parent or guardian changing the status in Settings.

Only access the `authorizationStatus` property on the [`main`](../../Dispatch/dispatchqueue/main.md) queue.

## See Also

### Tracking authorization changes
- [var $authorizationStatus: Published<AuthorizationStatus>.Publisher](./dollarauthorizationstatus.md)
  A publisher for the authorization status property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationcenter/authorizationstatus)*