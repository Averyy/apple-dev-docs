# Choosing the  Location Services Authorization to Request

**Framework**: Bundle Resources

Determine the authorization your app needs to access location data.

#### Overview

The authorization status that your app has determines if and when it receives location events. There are two types of authorization your app can request:

##### Prefer When in Use Authorization

Whenever possible, request only When In Use authorization. This mode has powerful features, allowing your app to:

- Access all available location services while the user is using the app. If the user stops using your app, any outstanding requests suspend until the user resumes using your app.
- Continue to get location updates even after your app enters the background, if you’ve enabled background location updates in your Xcode project. See [`Handling location updates in the background`](https://developer.apple.com/documentation/CoreLocation/handling-location-updates-in-the-background) for more information.
- Use location notification triggers to launch. If your app can rely on your user’s interaction, set up a [`UNLocationNotificationTrigger`](https://developer.apple.com/documentation/UserNotifications/UNLocationNotificationTrigger) to notify users when they enter a relevant region. When users click through the notification, the system launches the app, making it eligible to receive the location event. This method lets users decide at a relevant moment whether to share their location with your app.

Location services are available to apps with [`CLAuthorizationStatus.authorizedWhenInUse`](https://developer.apple.com/documentation/CoreLocation/CLAuthorizationStatus/authorizedWhenInUse) only while the app is “in use”. On all platforms that support When In Use authorization, an app is considered in use:

- When the app runs in the foreground.
- In the few seconds after an app leaves the foreground, a short grace period for your app to finish any current location tasks the user initiated.
- When the app shows the background location usage indicator ([`showsBackgroundLocationIndicator`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/showsBackgroundLocationIndicator)). On iOS, the indicator is a blue bar or pill at the top of the screen; on watchOS it’s a small icon.

For watchOS, the system always considers a complication on the current watch face to be in use. However, while the complication can receive location updates, you request authorization prompts from the main watch app. On watchOS there’s no way to opt out of showing the background location usage indicator.

##### Ask for Always Authorization

Your app might require Always authorization in some situations where users can’t or don’t want to engage with your app every time you need location information. You may need to ask for Always authorization if:

- Your app performs automated tasks during which a prompt might be inconvenient or undesirable. For example, if your app triggers automatic actions when the user enters a location, such as turning on the lights, your app may require Always authorization.
- Your app records numerous locations throughout the day, such as for a diary app. The user may prefer to allow Always authorization so your app can record locations even when it’s not in use, and without prompting the user.

Keep in mind that asking for authorization doesn’t guarantee your app will receive it. If you request Always authorization, the user has the option of granting your app When In Use authorization instead. You must always be prepared to run with When In Use authorization.

> **Note**:  If your app requests and receives When In Use authorization, you can make a separate request for Always authorization later. However, apps may make only one request for Always authorization.

While all platforms support When In Use authorization, the availability and functionality of Always authorization varies, as follows:

##### Request Authorization for Apps Running in Ios 12 and Earlier

Apps compiled with iOS 13 or later SDKs but running in iOS 12 or earlier will exhibit behavior consistent with iOS 12 for When In Use authorization. Specifically, in iOS 12 or earlier, some location services are only available to apps with Always authorization, as shown in this table:

| Service | When In Use | Always |
| --- | --- | --- |
| Standard location service | Supported | Supported |
| Significant-change location service | Not available | Supported |
| Visits service | Not available | Supported |
| Region monitoring | Not available | Supported |
| iBeacon ranging | Supported | Supported |
| Heading service | Supported | Supported |
| Geocoding services | Supported | Supported |

## See Also

- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](information-property-list/nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](information-property-list/nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/choosing-the-location-services-authorization-to-request)*