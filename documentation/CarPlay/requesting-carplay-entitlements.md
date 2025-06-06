# Requesting CarPlay Entitlements

**Framework**: Carplay

Configure your CarPlay-enabled app with the entitlements it requires.

#### Overview

To integrate with CarPlay, you must request the appropriate entitlement for your app’s category at [`CarPlay Contact Us`](https://developer.apple.comhttps://developer.apple.com/contact/carplay) and agree to the CarPlay Entitlement Addendum. Apple reviews each application using predefined criteria. If your request meets the criteria, Apple adds the entitlement to your developer account using managed capabilities. For more information, see [`Provisioning with managed capabilities`](https://developer.apple.comhttps://help.apple.com/developer-account/#/dev38c81d4cd).

After you receive the entitlement, you need to configure your Xcode project to use it, which involves several steps. You create or update an App ID, generate a provisioning profile, and add an `Entitlements.plist` file to your target. Your project’s code signing settings also require minor changes.

> **Note**:  CarPlay-enabled apps are subject to an additional set of App Store Review guidelines. For more information, see the [`CarPlay App Programming Guide`](https://developer.apple.comhttps://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf).

##### Add Carplay Capabilities to Your App Id

Update the App ID of your CarPlay-enabled app to include the necessary CarPlay capabilities by following these steps:

1. Complete the actions in [`Register an App ID`](https://developer.apple.comhttps://help.apple.com/developer-account/#/dev1b35d6f83) to create an App ID if you don’t already have one.
2. Sign in to your [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) account and select Certificates, Identifiers & Profiles.
3. Select Identifiers in the menu on the left.
4. Select your app’s App ID.
5. Choose the Additional Capabilities tab.
6. Enable the CarPlay capabilities that your app requires.
7. Click the Save button.
8. Create a new provisioning profile for the updated App ID. For more information, see [`Create a development provisioning profile`](https://developer.apple.comhttps://help.apple.com/developer-account/#/devf2eb157f8).

![A screenshot showing the Edit your App ID Configuration page in the developer portal. The Additional Capabilities tab is in a selected state and lists the available CarPlay capabilities. The CarPlay Audio App (CarPlay framework) capability is in an enabled state.](https://docs-assets.developer.apple.com/published/f69f20ddd7365e388da3ab9d6c088973/media-3703055%402x.png)

##### Import the Carplay Provisioning Profile

Configure your Xcode project to use the new provisioning profile when it code signs your CarPlay-enabled app by following these steps:

1. In Xcode, select your project in the Project navigator.
2. In the project editor, choose Signing & Capabilities.
3. Click All in the scope bar, and then deselect “Automatically manage signing”.
4. Click the Provisioning Profile pop-up menu and choose Download Profile.
5. Select your CarPlay provisioning profile from the left column and click Select Profile.

##### Add an Entitlements File

Use an `Entitlements.plist` file to specify the entitlements that your CarPlay-enabled app requires. They must match the capabilities you add to your App ID. CarPlay uses this file to determine the framework functionality to allow.

To create the entitlements file:

1. In Xcode, select your project in the Project navigator.
2. Choose File > New > File, select Property List from the Resource section, and click Next.
3. Enter `Entitlements` as the filename and click Create.
4. In the project editor, choose Build Settings.
5. Click All and Combined in the scope bar.
6. Use the search box to find the  setting.
7. Enter the full path of the `Entitlements.plist` file as the setting’s value.
8. Open the file in Xcode and add the applicable entitlement from the table below as a Boolean.

| Entitlement | Category |
| --- | --- |
| `com.apple.developer.carplay-audio` | Audio |
| `com.apple.developer.carplay-communication` | Communication |
| `com.apple.developer.carplay-charging` | EV Charging`` |
| `com.apple.developer.carplay-maps` | Navigation |
| `com.apple.developer.carplay-parking` | Parking`` |
| `com.apple.developer.carplay-quick-ordering` | Quick Food Ordering |

The following example shows the contents of a CarPlay-enabled app’s `Entitlements.plist` file with the audio entitlement:

```plist
<key>com.apple.developer.carplay-audio</key>
<true/>
```

##### Test Your Configuration

In Xcode, use a simulator to build and run your project. After Simulator launches, choose I/O > External Displays > CarPlay. Your app appears on the CarPlay Home screen.

## See Also

- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CarPlay/requesting-carplay-entitlements)*