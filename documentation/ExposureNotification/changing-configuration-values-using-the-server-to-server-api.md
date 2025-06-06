# Changing Configuration Values Using the Server‑to‑Server API

**Framework**: Exposure Notification

Update Exposure Notifications configuration values from a Public Health Authority’s server.

#### Overview

The Exposure Notifications feature reads configuration values to customize behavior for each region based on values provided by that region’s Public Health Authority (PHA). PHAs can push changes to these configuration values from their servers using the Exposure Notifications server-to-server API. A PHA might use the server-to-server API, for example, to automate changes under certain conditions, such as changing the polling interval when experiencing unusually high activity, or providing a configuration portal hosted on their own servers.

Exposure Notifications server-to-server API is located at the following URL:

```shell
https://gateway.icloud.com/enservice/v2/update/app/config
```

This API expects a POST request with a content-type of `application/json.` Requests must include both of the custom headers listed below to authenticate the request. The server rejects requests that the API can’t authenticate, and doesn’t make any changes to the existing configuration values.

The body of the POST request contains a JSON dictionary that uses the following keys:

This API responds with an HTTP response code, but won’t send a response body or any custom headers. If the API can make the requested changes, the API returns an HTTP `200` response code. If the API can’t change the values, it returns one of the following codes:

## See Also

- [Supporting Exposure Notifications Express](supporting-exposure-notifications-express.md)
  Configure servers to notify users of potential exposures to COVID-19 without an app.
- [Building an App to Notify Users of COVID-19 Exposure](building-an-app-to-notify-users-of-covid-19-exposure.md)
  Inform people when they may have been exposed to COVID-19.
- [Setting Up a Key Server](setting-up-a-key-server.md)
  Ensure that your server meets the requirements for supporting Exposure Notifications.
- [class ENManager](enmanager.md)
  A class that manages exposure notifications.
- [ENDeveloperRegion](../BundleResources/Information-Property-List/ENDeveloperRegion.md)
  A string that specifies the region that the app supports.
- [ENAPIVersion](../BundleResources/Information-Property-List/ENAPIVersion.md)
  A number that specifies the version of the API to use.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](testing-exposure-notifications-apps-in-ios-13-7-and-later.md)
  Perform end-to-end validation of Exposure Notifications apps on a device by manually loading configuration files.
- [Supporting Exposure Notifications in iOS 12.5](supporting-exposure-notifications-in-ios-12-5.md)
  Prepare your Exposure Notifications app to run on a previous version of iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/changing-configuration-values-using-the-server-to-server-api)*