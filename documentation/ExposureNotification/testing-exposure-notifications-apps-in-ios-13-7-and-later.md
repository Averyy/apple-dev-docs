# Testing Exposure Notifications Apps in iOS 13.7 and Later

**Framework**: Exposurenotification

Perform end-to-end validation of Exposure Notifications apps on a device by manually loading configuration files.

#### Overview

Exposure Notifications apps automatically download configuration information for the phone’s current region, such as the public key, public key version, and agency name. During development, those configuration files may not yet be available, or you may need to override the configuration values, for example, to point your app at a test server. You can manually set the default configuration values for your region by loading custom configuration files onto your development iPhone.

To load custom configuration files, you’ll need a Mac running Xcode, a device with your region’s Exposure Notifications app loaded on it, and the device profile you received from Apple when you registered as a PHA.

##### Enable the Developer Menu

To load a custom Exposure Notifications configuration, the device must have the Developer menu enabled in the Settings app. If you’ve used the device to test applications from Xcode, the menu is already enabled. To verify that it’s enabled, go to the Settings app and scroll down to make sure Developer is listed. Alternatively, type “developer” into the search bar and confirm it’s listed. Once you confirm the Developer menu is enabled, you’re ready to create your configuration file.

If your iPhone doesn’t have a Developer row in the Settings app, launch Xcode on a Mac, select Devices & Simulators from the Window menu, and plug your iPhone into your Mac. As Xcode prepares your device, a yellow bar appears at the top of the Devices & Simulators window. If you’ve never plugged your iPhone into this computer, you’ll be asked if you want to trust it. Select “Trust” on your iPhone. After a few minutes, the yellow bar disappears, which signals that your device is configured for development.

##### Create a Configuration File

Next, you need to create a configuration file that provides the configuration information your Exposure Notifications app needs to connect with your region’s servers. Start by copying the JSON below into a text file:

```json
{
    "appConfigs": [
        {
            "appBundleId": "[bundle identifier]",
            "config": {
                "V1Enable": true,
                "agencyColor": [
                    0,
                    0,
                    0
                ],
                "agencyDisplayName_EN_US": "PHA Agency",
                "agencyHeaderStyle": 0,
                "agencyHeaderSubtitle_EN_US": "The agency subtitle for Agency goes here",
                "agencyHeaderTextColor": [
                    0.5,
                    1,
                    0.5
                ],
                "agencyImage": "agencyImage",
                "agencyMessage_EN_US": "Agency PHA has an agency Message for you",
                "agencyRegionName_EN_US": "Region",
                "applicationBackgroundRuntimeIntervalinHours": 2,
                "callbackIntervalInMin": 240,
                "detectExposureDailyLimit": 20,
                "detectExposureNKDLimit": 6,
                "dynamicAlgorithmEnabled": true,
                "dynamicThrottleDownAdvDensity": 6,
                "dynamicThrottleDownDurationInSeconds": 216,
                "dynamicThrottleDownRSSI": -55,
                "dynamicThrottleUpAdvDensity": 20,
                "dynamicThrottleUpDurationInMinutes": 900,
                "enEnabled": true,
                "enVersion": 1,
                "enableRecursiveType": false,
                "exposureMatching": true,
                "forceAPWakeIntervalInMinutesThreshold": 5,
                "hasStateRegions": false,
                "isMatchingRestrictedRegion": false,
                "maxMatchingAttempts": 7,
                "maxTtkMatchAttempt": 8,
                "maxTtkMatchAttemptPerDay": 9,
                "numberOfAdvSamplesForRPIThreshold": 1,
                "osTriggeredAppRunTimeInSeconds": 300,
                "privacyParameterInputCandence": 7,
                "regionDisabledTransitionGracePeriodMinutes": 1440,
                "regionTransitionGracePeriodInMinutes": 180,
                "reportTypeRecursiveWeight": 100,
                "rpiAdvertisementToleranceInMinutes": 120,
                "rpiDuplicateAdvertisementToleranceInMinutes": 20,
                "serverConfigVersion": 1,
                "status": "approved"
            },
            "countryCode": "[country code]",
            "publicKey": "[public key]",
            "publicKeyVersion": "[public key version]",
            "signAuthorityName": "Agency Sample Authority",
            "state": ""
        }
    ]
}
```

Modify the JSON so the field values match your desired configuration. At a minimum, you must replace:

- `[bundle identifier]` with your app’s actual bundle identifier
- `[public key]` with the most recent public key you registered with Apple
- `[public key version]` with the version number of your public key as a string (for example, `v2`)
- `[countryCode]` with the `ENDeveloperRegion` value from your app’s `info.plist`

If your app’s region includes both a country and subdivision code, such as “US-CA”, only include the country code (for example “US”), not the entire region code in the `countryCode` field, and then populate the `state` field with the full region code (for example, “US-CA”, not just “CA”).

After you’ve made your changes, save the file somewhere on your Mac with the name `Test_Config.json`. If you’re testing in iOS 14.1 or later, copy `Test_Config.json` to the Files app on your iPhone by using AirDrop, or by adding it to the iCloud Drive folder on your Mac and then waiting for it to sync to your iPhone. If you’re testing in iOS 14.0 or iOS 13.7, you’ll need to convert the JSON file you created into a property list before copying it to your iPhone.

##### Convert the Json File to a Property List Ios 14 and Ios 137

To convert the JSON file you created into a property list in iOS 14.0 or iOS 13.7, open the Terminal app on your Mac, use `cd` to navigate to the directory where you saved T`est_Config.json`, then type the following command to generate the configuration property list to load onto your iPhone:

```swift
plutil -convert xml1 Test_Config.json -o Test_Config.plist
```

The `plutil` command converts your JSON file into a new `.plist` file called `Test_Config.plist` and places it in the same directory as the original JSON file. Copy that new file to the Files app on your iPhone by using AirDrop, or by adding the file to the iCloud Drive folder on your Mac and then waiting for it to sync to your iPhone.

##### Load the Configuration File

Once the configuration file is available in the Files app on your iPhone, open the Settings app, scroll down, and tap Developer. Select Exposure Notifications, then tap Developer Server Configuration to enable it, and choose Override Configuration File. Your phone will prompt you for the location of the configuration file. Select `Test_Config.json` if you’re testing in iOS 14.1 or later, or `Test_Config.plist` if testing in iOS 14.0 or iOS 13.7. After you select the configuration file, you’ll receive a notification that says, “Successfully set override configuration file”.

> **Note**:  if you don’t see an Exposure Notifications option under the Develop menu in the Settings app, you may need to install the Exposure Notifications profile provided by Apple, which enables that option. If you have installed the profile and still don’t see the option, [`contact Apple Developer Technical Support`](https://developer.apple.comhttps://developer.apple.com/membercenter/index.action#requestTechSupport).

Navigate back to the top level of the Settings app and tap Exposure Notifications. Select Turn on Exposure Notifications and then select your app’s region. Once you do this, your phone will use the information from the custom configuration file. When you want to stop using your custom configuration file, disable Developer Server Configuration under Exposure Notifications in the Developer section of the Settings app.

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
- [Changing Configuration Values Using the Server‑to‑Server API](changing-configuration-values-using-the-server-to-server-api.md)
  Update Exposure Notifications configuration values from a Public Health Authority’s server.
- [Supporting Exposure Notifications in iOS 12.5](supporting-exposure-notifications-in-ios-12-5.md)
  Prepare your Exposure Notifications app to run on a previous version of iOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExposureNotification/testing-exposure-notifications-apps-in-ios-13-7-and-later)*