# Creating a location push service extension

**Framework**: Core Location

Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.

#### Overview

The Location Push Service Extension (LPSE), available starting in iOS 15, is a power-efficient way to query locations on iOS or iPadOS devices, even when your app isn’t running.

LPSE is available for apps that allow individuals to share their location with other people that they explicitly approve. It’s also available for use with apps that alert the nearest first-responders to a time-sensitive medical emergency. To use LPSE, you need to add the capability to the extension in Xcode.

When your app includes this extension, the system activates it when it receives an Apple Push Notification service (APNs) `location` push (a *push event*) from your server. Your app must ask for and receive  [`CLServiceSession.AuthorizationRequirement.always`](CLServiceSession-pt7n/AuthorizationRequirement/always.md) authorization from someone before the extension is eligible to receive push events. For more information about requesting “always” authorization, see [`Requesting authorization to use location services`](requesting-authorization-to-use-location-services.md) and [`init(authorization:)`](CLServiceSession-pt7n/init(authorization:).md) .

Once a person authorizes location data, the extension can query their location and process it for your app. Your server sends requests with the `location` push type to APNs. For more information about sending requests to APNs, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns).

##### Understand the Limitations of Lpse and Push Event Allocations

The following list details the operational constraints and expectation for apps that adopt the LPSE:

- LPSE push events are a mechanism to wake the extension so it can report on device location.
- Use push events sparingly: don’t send a follow-up push event if you sent one recently; hand location delivery off to your app for long-running or high-frequency use cases. Use the CoreLocation API — for example, [`liveUpdates(_:)`](cllocationupdate/liveupdates(_:).md) — to wake your main app to continue the reporting task when the extension’s time is up.
- The system limits the number of push events a device may receive to approximately 360 events in a 24-hour period, to help protect battery life of the device.
- As an app receives push events, the system subtracts them from the total available; the system also replenishes them at a rate of 1 every few minutes, up to the maximum daily allotment.
- Once a device receives a push event from the network, the system checks to see whether the extension may handle the event before invoking the extension to do so.
- If no more push event handling capacity exists, the system unregisters from the push topic to protect battery life for some time; the device doesn’t receive push events during this period.
- There’s no way to find out how many push events are remaining at any given time.

##### Configure Your Xcode Project

To include Location Push Service Extension in your app, configure entitlements, capabilities, and keys for your Xcode project in these steps:

- Add the Location Push Server Extension entitlement. For instructions on adding this entitlement, see [`Location Push Service Extension`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.location.push).
- Enable your app to receive Apple Push Notification service (APNs) pushes by adding the Push Notifications capability. For more information, see [`Registering your app with APNs`](https://developer.apple.com/documentation/UserNotifications/registering-your-app-with-apns).
- Configure the purpose strings your app provides for the location service authorization prompts. For more information, see [`Requesting authorization to use location services`](requesting-authorization-to-use-location-services.md).

##### Add a Location Push Service Extension Target

Add a new target using the Location Push Service Extension template.

1. Open your iOS app project in Xcode.
2. Choose File > New > Target.
3. Select Location Push Service Extension from the iOS Application Extension group.
4. Click Next.
5. Specify the name of your extension and configure the language and other options.
6. Click Finish.

Xcode creates a subclass of [`CLLocationPushServiceExtension`](CLLocationPushServiceExtension.md) to get you started.

##### Implement Location Push Functionality

To support location push functionality, implement these steps in your extension, app, and server:

1. In your service extension, implement the [`CLLocationPushServiceExtension`](CLLocationPushServiceExtension.md) protocol.
2. In your service extension, implement the [`liveUpdates(_:)`](cllocationupdate/liveupdates(_:).md) method to handle the result of the location request, and process location data it receives from the network.
3. In your app, call [`startMonitoringLocationPushes(completion:)`](cllocationmanager/startmonitoringlocationpushes(completion:).md) to receive an APNs token as `Data`, and send it to your server. Your server uses this token when it creates APNs pushes.
4. From your server, request location information by sending a `location` push request to APNs.

When a person using your app indicates they want to use this sharing feature, create a [`CLServiceSession`](CLServiceSession-pt7n.md)  instance using `CLServiceSession(requiring:.Always)`. Keep an instance available in both your app and in the app extension whenever the app or extension runs, unless and until a person opts out of the authorization to use the service. Use the  [`CLServiceSession.Diagnostics`](CLServiceSession-pt7n/Diagnostics-swift.class.md) iterator to check for diagnostic information about permission to use the service. For example, if the iterator returns [`alwaysAuthorizationDenied`](CLServiceSessionDiagnostic/alwaysAuthorizationDenied.md), this means that LPSE is not working and you need to apply business logic to determine if this indicates an implicit opt-out of the previous permission, or if your app needs to direct someone to Settings to grant “Always authorization” for location services for your app.

For more information, see the [`CLServiceSession`](CLServiceSession-pt7n.md) documentation.

> ❗ **Important**:  Help protect a person’s privacy when your app handles location data. Use end-to-end encryption to provide enhanced security if your app moves location data off someone’s device, including transmitting it to a server or to another person. For more information, see [`Protecting the User’s Privacy`](https://developer.apple.com/documentation/UIKit/protecting-the-user-s-privacy).

##### Send Location Push Requests From Your Server

When someone requests the location of another person, your app sends the request to your server, which sends a location push request to APNs. Ensure that your APNs `POST` request contains the following fields for a `location` push type:

- **`method`**: (Required) The value is `POST`.
- **`path`**: (Required) The path to the device token. The value of this header is `/3/device/<device_token>`, where `<device_token>` is the hexadecimal identifier of the user’s device. Your app receives the token when it calls [`startMonitoringLocationPushes(completion:)`](cllocationmanager/startmonitoringlocationpushes(completion:).md) to start monitoring location pushes.
- **`authorization`**: (Required for token-based authentication) The value of this header is `bearer <provider_token>`, where `<provider_token>` is the encrypted token that authorizes you to send notifications for the specified topic. For more information, see [`Establishing a token-based connection to APNs`](https://developer.apple.com/documentation/UserNotifications/establishing-a-token-based-connection-to-apns).
- **`apns-topic`**: The topic is your app’s bundle ID with the suffix `".location-query"`.
- **`apns-push-type`**: (Recommended) The value of this header is `location`.

For more information about sending APNs requests and using command-line tools to do so, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns) and [`Sending push notifications using command-line tools`](https://developer.apple.com/documentation/UserNotifications/sending-push-notifications-using-command-line-tools).

## See Also

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)
  Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md)
  Configure your app to receive location updates when it isn’t running in the foreground.
- [class CLLocation](cllocation.md)
  The latitude, longitude, and course information reported by the system.
- [struct CLLocationCoordinate2D](cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [class CLFloor](clfloor.md)
  The floor of a building on which the user’s device is located.
- [class CLVisit](clvisit.md)
  Information about the user’s location during a specific period of time.
- [class CLLocationSourceInformation](cllocationsourceinformation.md)
  Information about the source that provides a location.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md)
  Define boundaries and act on user location updates.
- [class CLServiceSession](clservicesession-pt7n.md)
  An object that provides diagnostics about an app’s authorization to use location services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/creating-a-location-push-service-extension)*