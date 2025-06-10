# Installing apps from an alternative marketplace

**Framework**: MarketplaceKit

Manage the installation of apps that developers distribute from your marketplace app.

#### Overview

To install apps that others distribute on your marketplace, call the [`AppLibrary`](applibrary.md) installation functions. The system enforces that calls displaying the install sheet need to source from the callback of an [`ActionButton`](actionbutton.md). This ensures that app installation occurs as the result of a person’s interaction with your marketplace app.

In processing the request, the system retrieves a license from your web server. Provide the license by implementing the [`App License Delivery SDK`](https://developer.apple.com/documentation/AppLicenseDeliverySDK) on a Swift server with an endpoint that the device’s operating system discovers by looking up a standard URL scheme.

If your marketplace requires authentication to download apps — for example, a purchase or log in — implement an authentication service that the device can query to decorate the headers of its communication with your endpoints. To set the header, and handle any network failures, provide a [`MarketplaceExtension`](marketplaceextension.md) in your app and implement its callbacks.

When the system receives a license, it requests that licensed app from your web server. Publish two endpoints that field requests for apps, including restore requests for new apps, and update requests. Using MarketplaceKit, handle any errors that might occur as the system communicates with your server, and provide people with visual status during app management tasks that might be long-running, such as installing an app.

#### Define the Request Header

Bundle an extension with your marketplace to define authorization headers for requests to your server. Implement the [`MarketplaceExtension`](marketplaceextension.md) method [`additionalHeaders(for:account:)`](marketplaceextension/additionalheaders(for:account:).md).

The system calls your implementation of `additionalHeaders` to add custom information that you choose in each communication it makes with your web server. MarketplaceKit doesn’t require a specific authentication method for the installation of an alternative marketplace’s apps. You can use OAuth 2.0 or add custom information to associate the communication with the person signed in, or the person’s unique device. This effectively authorizes the system to act on the person’s behalf on subsequent calls to your web server for app licenses or alternative distribution packages.

If an access token or subscription expires, return an HTTP failure code from your marketplace server. The system calls your [`MarketplaceExtension`](marketplaceextension.md) method  [`requestFailed(with:)`](marketplaceextension/requestfailed(with:).md) implementation to correct the issue. If the failure results from:

- An expired subscription, set a flag to present an e-commerce flow within your alternative marketplace app.
- An invalid access token, reauthenticate the person according to [`Reauthenticate a person in your marketplace app or extension`](reauthenticating-a-person-to-manage-apps#Reauthenticate-a-person-in-your-marketplace-app-or-extension.md).

#### Request Installation From an Alternative App Marketplace

Your app requests app installation using MarketplaceKit API. The system enforces that installation requests source from a person’s interaction with your app’s UI. In other words, your app can install another app only when a person requests it by tapping a button. MarketplaceKit provides the [`ActionButton`](actionbutton.md) class for this purpose.

The following code defines an action button that presents the app install sheet for an app identified by the argument [`AppleItemID`](appleitemid.md). The code takes a `confirmInstall` closure, and confirms the installation with an install verification token and authentication context.

```swift
class ViewController: UIViewController {

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Describe the app to install. 
    let installMetadata = InstallMetadata( 
        account: "Test", 
        appleItemID: 6476788646, 
        alternativeDistributionPackage: URL(
            string: "https://example.com/packages/6476788646/version/1")!, 
        isUpdate: false)
    
    // Define the app's landing page.  
    installMetadata.appShareURL = URL(
        string: "https://example.com/apps/6476788646")!
    
    // Pass the app info to an Install button.
    let button = ActionButton(
        action: .install(
            InstallConfiguration(
                install: installMetadata, 
                confirmInstall: {
                    // Perform e-commerce, if needed.
                    return .confirmed(
                        installVerificationToken: installVerificationToken, 
                           authenticationContext: myLAContext
                    )
                }
            )
        )
    )    

    // Configure the button. 
    button.addTarget(self, action: #selector(installAction), for: .touchUpInside)
    button.label = "Install"
    button.fontSize = 18
    button.tintColor = .white
    button.backgroundColor = .systemBlue
    button.size = CGSize(width: 200, height: 75)
    button.cornerRadius = 15
    button.isEnabled = true
    button.center = self.view.center
    self.view.addSubview(button)
```

If an app requires a purchase before installation, modify the `confirmInstall` closure to present a custom UI and external purchase flow that you implement in your app.

#### Retrieve a License for the App From Your Web Server

If your website doesn’t require authentication or the system is already successfully authorized to act on behalf of the page visitor, the system requests an app license from your web server. To process license requests, your web server implements an endpoint that serves generated licenses by using [`App License Delivery SDK`](https://developer.apple.com/documentation/AppLicenseDeliverySDK).

#### Serve a Restore Request

When your server responds with a license, the system then requests the app. To determine the endpoint to call, the system checks your `marketplace-kit` configuration file at the following relative URL:

```None
<fully-qualified-domain>/.well-known/marketplace-kit
```

Inside the file, define an endpoint to handle `restore` requests that the system makes to retrieve a specific app version:

```None
"restore": "<fully-qualified-domain>/PATH",
```

The system calls your restore endpoint with the following example POST:

```json
{ 
    "apps": [
        { "appleItemId": "<the app's appleItemID>",
        "appleVersionId" : "<version number>" }
    ], 
    "platform" : "iOS" | "iPadOS",
    "osVersion" : "17.4"
}
```

The POST contains the following fields:

| Request field | description |
| --- | --- |
| `apps` | An array that contains an object for each app in the request.  Each object in the array consists of an identifier ([`AppleItemID`](appleitemid.md)) and version ([`AppleVersionID`](appleversionid.md)) for the requested app. |
| `platform` | A string that identifies the platform of the installing device. |
| `osVersion` | A string that identifies the operating system version of the installing device. |

Compare the `platform` and `osVersion` fields to those contained within the app’s manifest to confirm that your alternative distribution package supports the device attempting to install it.

> ❗ **Important**: Host the file using `https://` with a valid certificate. Don’t use redirects. For more information, see [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains).

If downloading your app requires authorization and the system communicates with your endpoint without a valid access token, respond to the call with a status that requests reauthentication. An invalid access token can result from token expiration, or the restoration of a device from a backup. For more information, see [`Reauthenticating a person to manage apps`](reauthenticating-a-person-to-manage-apps.md).

Otherwise, send your app in response by supplying a URL in the `restores` element to the alternative distribution package for the requested app version:

```json
{
    "restores": [
        { "appleItemId": "<the app's appleItemID>",
        "appleVersionId": "<version number>",
        "alternativeDistributionPackage": "<fully qualified domain>/PATH",
        "installVerificationToken" : <required-string>
        "appShareURL" : <URL> }
    ]
}
```

The `"restores"` array in the response contains an object for each requested app. Each object in the array contains the following fields:

| Response field | description |
| --- | --- |
| `appleItemId` | An identifier for a requested app. For more information, see [`AppleItemID`](appleitemid.md). |
| `appleVersionId` | A version number that corresponds to the alternative distribution package. For more information, see  [`AppleVersionID`](appleversionid.md). |
| `alternativeDistributionPackage` | The app’s alternative distribution package in the assembled format described in [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md). This value has unique domain-matching requirements; for more information, see [`MarketplaceKitURIScheme`](marketplacekiturischeme.md). |
| `installVerificationToken` | A JSON web signature that [`MarketplaceKit`](MarketplaceKit.md) requires for installations. For more information, see [`Supplying an install verification token`](supplying-an-install-verification-token.md). |
| `appShareURL` | An optional URL to a product landing page for the app on your marketplace website. The operating system populates the value in the Share Sheet when a person touches and holds the app’s icon on the Home Screen. |

#### Serve an App Update Request

When a person requests an update to an installed app, or when Automatic Updates are on, the system sends a request similar to a restore. Add the `updates` endpoint in your server’s `marketplace-kit` configuration:

```None
<fully-qualified-domain>/.well-known/marketplace-kit
```

Set `url` to your server’s endpoint that handles app update requests:

```json
"updates": {
    "url" : "<fully-qualified-domain>/PATH",
    "pollingInterval": 24
```

The `pollingInterval` property is required. Set it to the minimum number of hours that the system waits to check for app updates. For example, if you set `pollingInterval` to `48`, the system calls your `updates` endpoint at most every 48 hours. In any case, the system calls your `updates` endpoint at most once every 24 hours.

The system sends an update POST to your endpoint, such as:

```json
{
    "apps" : [
        {
            "appleItemId" : "<the app's appleItemID>",
            "appleVersionId" : "<version number>",
        },
        {
            "appleItemId" : "<a second app's appleItemID>",
            "appleVersionId" : "<version number>"
        }
    ],
    "platform" : "iOS" | "iPadOS",
    "osVersion" : "17.0"    
}
```

The request contains the same fields as the POST for serving a restore request. For more information see the table above in [`Serve a restore request`](https://developer.apple.com#Serve-a-restore-request).

In response, your endpoint gives the alternative distribution package(s) in the `updates` element for apps matching the request criteria:

```json
{
    "updates": [
        { "appleItemId": "<the app's appleItemID>",
        "appleVersionId": "<version number>",
        "alternativeDistributionPackage": "<fully qualified domain>/PATH",
        "bundleVersion" : "1",
        "shortVersionString" : "1.0.14",
        "installVerificationToken" : <required-string>
        "appShareURL" : <URL> }
    ]
}
```

The `"restores"` array in the response contains an object for each requested app. Each object in the array contains the following fields:

| Response field | description |
| --- | --- |
| `appleItemId` | An identifier for an app to update. For more information, see [`AppleItemID`](appleitemid.md). |
| `appleVersionId` | A version number that corresponds to the alternative distribution package. For more information, see  [`AppleVersionID`](appleversionid.md). |
| `alternativeDistributionPackage` | The requested app’s alternative distribution package in the assembled format described in [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md). This value has unique domain-matching requirements; for more information, see [`MarketplaceKitURIScheme`](marketplacekiturischeme.md). |
| `bundleVersion` | The app’s bundle version. |
| `shortVersionString` | The app’s short version string. |
| `installVerificationToken` | A JSON web signature that [`MarketplaceKit`](MarketplaceKit.md) requires for installations. For more information, see [`Supplying an install verification token`](supplying-an-install-verification-token.md). |
| `appShareURL` | An optional URL to a product landing page for the app on your marketplace website. The operating system populates the value in the Share Sheet when a person touches and holds the app’s icon on the Home Screen. |

#### Indicate App Unavailability

If a device requests an app that’s not available on your alternative marketplace, then your marketplace responds with a `"failures"` array that includes the unavailable apps:

```json
{
    "restores": [ { ... } ],
    "updates": [ { ... } ],
    "failures": [
        { "appleItemId": "10737747186",
        "appleVersionId": "2000004563",
        "failure": { "code" : 404, "description": "App unavailable." } }
    ]
}
```

The `"failures"` array in the response contains an object for each requested app you fail to provide:

| failures field | description |
| --- | --- |
| `appleItemId` | An identifier for the app your server fails to provide. For more information, see [`AppleItemID`](appleitemid.md). |
| `appleVersionId` | The version of the app your server fails to provide. For more information, see  [`AppleVersionID`](appleversionid.md). |

For a description of the `"restore"` and `"update"` fields, see [`Serve a restore request`](installing-apps-from-an-alternative-marketplace#Serve-a-restore-request.md) and [`Serve an app update request`](installing-apps-from-an-alternative-marketplace#Serve-an-app-update-request.md).

An app might be unavailable if the developer removes it from sale or if Apple sends an app take-down request. A device that’s restoring from a backup might be uninformed of the removal as it requests the app as part of the restore process.

To indicate the app isn’t available in the response, set `"code"` to `404`. If the request intiates from someone’s actions, such as tapping a darkened app icon while restoring their device from a backup, the system displays an informative prompt on the Home Screen that reads:

```None
App Not Available 
"App 1" not available from Megabyte Mart.
```

#### Override the Marketplacekit Endpoint for an App

To handle a specific app differently, modify the `marketplace-kit` file to add a configuration just for that app using the `"overridesByAppleItemID"` element. Inside, define an `"appleItemId"` element that contains a copy of the `marketplace-kit` configuration, differing in just the ways necessary to process the specific app.

```json
{
    "overridesByAppleItemID":
    {
        "<appleItemId>":
        {
            "restore": "<fully-qualified-domain>/PATH",
            "updates":
            {
                "url": "<fully-qualified-domain>/PATH",
                "pollingInterval": <polling-interval>
            },
            "license": "..."
        }
    }
    // The default configuration follows: 
    "restore": "<fully-qualified-domain>/PATH",
    "updates":
    {
        "url": "<fully-qualified-domain>/PATH",
        "pollingInterval": <polling-interval>
    },
    "license": "..." 
}
```

Add the `"overridesByAppleItemID"` element to the bottom of your `marketplace-kit` configuration file.

You can override the `marketplace-kit` endpoint for many reasons. For example, to route requests for a specific app on your marketplace to a different endpoint for processing.

#### Show Progress for App Downloads

To provide a responsive installation experience, give visual feedback while installation is in progress. Display your own custom UI according to the [`progress`](applibrary/app/installation-swift.struct/progress.md) object to provide visual feedback on the state of a given installation. Convey the progress in a way that works for your app; MarketplaceKit doesn’t provide a predetermined UI for progress.

## See Also

- [Processing alternative app marketplace notifications](processing-alternative-marketplace-notifications.md)
  Manage the addition and removal of apps available on your alternative marketplace.
- [Ingesting an alternative distribution package](ingesting-an-alternative-distribution-package.md)
  Process an available app version from App Store Connect and store it for download from your server.
- [Installing your app from your website](installing-your-app-from-your-website.md)
  Manage the installation of an app that you develop and distribute through your website.
- [Supplying an install verification token](supplying-an-install-verification-token.md)
  Support the installation of alternative distribution apps by creating signed JSON web tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installing-apps-from-an-alternative-marketplace)*