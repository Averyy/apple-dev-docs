# Manage Settings on Devices in a Family Sharing Group

**Framework**: ManagedSettings

Empower parents and guardians to configure constraints on other devices while preserving the family’s privacy.

#### Overview

Use Managed Settings together with [`ManagedSettingsUI`](https://developer.apple.com/documentation/ManagedSettingsUI), [`DeviceActivity`](https://developer.apple.com/documentation/DeviceActivity), and [`FamilyControls`](https://developer.apple.com/documentation/FamilyControls) to manage a device’s settings while preserving the user’s privacy. Managed Settings can’t function without a parent or guardian in the same Family Sharing group authorizing your app using Family Controls. To help implement time-based settings, Device Activity executes your code on a schedule without a child running your app. The parent or guardian in the Family Sharing group makes the decisions about setting management, and no one outside of the group can see the apps the group uses or the activities they participate in on their devices.

##### Request Authorization for Your App

The Family Controls framework contributes privacy-preserving capabilities to the suite of development tools. When you create an app with the Managed Settings framework, users must authorize your app when they open it for the first time on a device. After a parent or guardian authorizes your app, only a parent or guardian can delete your app. Family Controls uses tokens to represent applications and websites on a user’s device. The tokens ensure that no one outside of the user’s Family Sharing group can see the apps the family uses or the websites they visit.

The following code shows how to request authorization from a user to use your app:

```swift
import FamilyControls 

AuthorizationCenter.shared.requestAuthorization { result in 
    switch result {
        case .success():
            //...
        case .failure(let error):
           //...
    }
}
```

##### Handle Time Limits and Schedule Constraints

Since a child might not use your app independently, Device Activity executes your code even when your app isn’t running. A parent or guardian can set device usage schedules and time limits with your app. The system notifies your app when scheduled events occur and when usage approaches time limits. You can provide notifications on a device to warn the user that a scheduled event or time limit is approaching.

Device Activity tracks and notifies your app about device usage, according to controls the parent or guardian creates in your app with Family Controls. For example, your app can enable a parent or guardian to specify a time limit of one hour of activity per day. When the child’s device reaches that limit, the system activates your app extension to handle the event. Your app can choose to handle that event by updating managed settings, such as adding an app to the list of blocked applications.

## See Also

- [Confirming the Effective TV and Movie Ratings](readingmedia.md)
  Read the media rating on a device and determine what media to display on your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/connectionwithframeworks)*