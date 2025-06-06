# Configuring your project for sensor reading

**Framework**: SensorKit

Add metadata to your app to attain system and user permission to access sensor data.

#### Overview

If Apple approves your idea for a research-study app, you can read sensor data from devices after receiving the userʼs permission. Once Apple approves your app, you receive an entitlement that enables your app to read sensor data. In accordance with the approval, you also need to comply with Appleʼs privacy policy.

When your app attempts to read sensor information for the first time on a person’s device, the system presents a sheet that explains your app’s research study and the information your app collects. The sheet prompts people to approve access to personal information at a granular level, and your app needs to tell people which information is essential to the study. You supply the study purpose, requested sensors, and privacy policy URL in the project’s `Info.plist`.

For more information, see [`Sensor & Usage Data & Privacy`](https://developer.apple.comhttps://www.apple.com/legal/privacy/data/en/sensor-usage-data/).

##### Request the Sensor Reader Entitlement

To use SensorKit, the OS requires the [`com.apple.developer.sensorkit.reader.allow`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensorkit.reader.allow) entitlement in your app’s code signature. Apple only grants the entitlement for approved research studies. If you’re interested in accessing SensorKit data for your study, submit a research proposal and request the entitlement. For more information, see [`Accessing SensorKit Data`](https://developer.apple.comhttps://www.researchandcare.org/resources/accessing-sensorkit-data/).

##### Create a Manual Provisioning Profile

Xcode requires a manual provisioning profile that includes an explicit App ID to code-sign your app with the sensor reader entitlement.

To create the explicit App ID, sign in to Apple Developer, register an App ID for your SensorKit project, and enable the sensor reader entitlement under Additional Capabilities on the [`Certificates, Identifiers, & Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources/certificates/list) page. For more information, see [`Register an App ID`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-identifiers/register-an-app-id).

To create the manual provisioning profile, select Profiles from the sidebar, click the add button (+) in the upper-left, and select the iOS App Development profile type. For more information, see [`Create a development provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-profiles/create-a-development-provisioning-profile).

Install the provisioning profile by downloading it and dragging it on to the Xcode icon in the Dock. Alternatively, you can select the Download Manual Profiles option by choosing Xcode > Preferences > Accounts and selecting your Apple ID and applicable team. For more information, see [`Download manual provisioning profiles`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/?/deva899b4fe5#/deva899b4fe5).

##### Configure Xcode for Signing

Define a bundle ID in Xcode for your App ID by selecting your target in the project editor and clicking General. For more information, see [`Set the bundle ID`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/deve21d0239c).

![Screenshot of the project target’s General tab. Under the Identity section, the Bundle Identifier text field reflects a value that matches the App ID associated with the provisioning profile.](https://docs-assets.developer.apple.com/published/91ee9ae6f487ded7a99f5cfb70a36b54/media-3924188%402x.png)

Add a new property list file to your project named `[Your App Name].entitlements` if it doesn’t already exist. Add a key titled `com.apple.developer.sensorkit.reader.allow` with the type Array, and add a string value for each sensor your app uses:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict> 
    <key>com.apple.developer.sensorkit.reader.allow</key>
    <array> 
        <string>on-wrist</string>
        <string>ambient-light-sensor</string>
        <string>motion-accelerometer</string>
        <string>motion-rotation-rate</string>
        <string>visits</string>
        <string>pedometer</string>
        <string>device-usage</string>
        <string>messages-usage</string>
        <string>phone-usage</string>
        <string>keyboard-metrics</string> 
</array></dict></plist>
```

The code-signing entitlements file for the above raw property list appears as follows in Xcode:

![Screenshot of the code signing entitlements property list file in Xcode. The list’s root node contains a Array key titled com.apple.developer.sensorkit.reader.allow. The array contains String values for each sensor the app requests, which are: on-wrist, ambient-light-sensor, motion-accelerometer, motion-rotation-rate, visits, pedometer, device-usage, messages-usage, phone-usage, and keyboard-metrics.](https://docs-assets.developer.apple.com/published/0f02fccfc21f1537d4dfac88eca00fd0/media-3924189%402x.png)

To sign your app with the manual provisioning profile and sensor reader entitlement, set your targetʼs build settings as follows:

- Code Signing Entitlements to the entitlements file
- Code Signing Identity to `Apple Developer`
- Code Signing Style to `Manual`
- Provisioning Profile to the manual provisioning profile you created

![Screenshot of the project target’s build settings. The code signing entitlements setting reflects the custom code signing entitlements file name. The code signing identity is set to iOS developer. Code signing style is manual. And the provisioning profile build setting reflects the name of the explicit provisioning profile.](https://docs-assets.developer.apple.com/published/62ff7067e9c673a6bf589fbd7215b42a/media-3924190%402x.png)

##### Describe the Purpose of Your Study

The system presents the Research Sensor & Usage Data Request sheet that introduces your appʼs study to people. Define a short description of your appʼs research purpose with the usage description `Info.plist` key.

```plist
<key>NSSensorKitUsageDescription</key>
<string>This is my app&apos;s SensorKit usage description.</string>
```

The sheet displays the research purpose in the App Research Purpose banner.

![Screenshot of the Research Sensor & Usage Data Request sheet that introduces the app’s study. The sheet displays the app’s SensorKit usage description under the App Research Purpose banner.](https://docs-assets.developer.apple.com/published/87538d610da299dfd44a740a01ab3eb1/media-3928456%402x.png)

##### Link Your Apps Privacy Policy

Add a link to your privacy-policy webpage in your projectʼs `Info.plist` using the [`NSSensorKitPrivacyPolicyURL`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitPrivacyPolicyURL) key.

```plist
<key>NSSensorKitPrivacyPolicyURL</key>
<string>https://my-site.example.com/privacy-policy/</string>
```

The sheet displays a link to your app’s privacy policy below the description of your study.

![Screenshot of the Research Sensor & Usage Data Request sheet that introduces the app’s study. The View App Privacy Policy link is highlighted below the app’s research purpose.](https://docs-assets.developer.apple.com/published/f9d7a9b0eac3c48762a1b034566ebed1/media-3683202%402x.png)

##### Explain How Your App Uses the Data

The sheet also explains what your app intends to do with the information it collects with a particular sensor. You provide this intent per sensor by adding the sensorʼs usage-detail key in your appʼs `info.plist`. For example, add the [`SRSensorUsageMotion`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSensorKitUsageDetail/SRSensorUsageMotion) key when you use the [`accelerometer`](srsensor/accelerometer.md) property. For the other sensor-specific usage keys, see the [`SRSensor`](srsensor.md) property descriptions.

```plist
<key>NSSensorKitUsageDetail</key>
<dict> 
    <key>SRSensorUsageMotion</key>
    <dict> 
        <key>Description</key> 
        <string>This describes how my app uses motion data.</string>
    </dict> 
</dict>
```

To begin reading sensor data, call `requestAuthorization(sensors:completion:)` to pass in the sensors your app records.

```swift
// A sensor for ambient light information.
let reader = SRSensorReader(sensor: .ambientLightSensor)

// Displays the authorization approval prompt. 
func requestAuthorization() {
    SRSensorReader.requestAuthorization(
        sensors [.ambientLightSensor]) { (error: Error?) in
        if let error = error {
            fatalError("Sensor authorization failed due to: \(error)") 
        } else {
            print("""
                User dismissed the authorization prompt. 
                Awaiting authorization status changes.
            """) 
        } } }

// Sets up the view. 
override func viewDidLoad() {

    // Listen for authorization status changes.
    reader.delegate = self
}

```

The first time your app requests authorization for a particular sensor, the sheet prompts for user approval and displays the sensorʼs corresponding usage-detail string.

![Screenshot of the Research Sensor & Usage Data Request sheet’s second page. A banner reads “How the study will use this data” above text that reads, “This describes how my app uses motion data.”](https://docs-assets.developer.apple.com/published/c5f5159fb33c1a5c9b45136890b92e34/media-3683199%402x.png)

##### Specify the Sensors Your App Requires

Through the sheet, people approve each sensor individually by tapping Allow Collection & Sharing or Don’t Allow Collection & Sharing.

![Screenshot of the Research Sensor & Usage Data Request sheet’s second page that highlights two buttons at the bottom. The upper button reads “Allow Collection & Sharing”. The lower button reads, “Don’t Allow Collection and Sharing”.](https://docs-assets.developer.apple.com/published/9dfd6a81c4382a107e5d9faa6b9c6393/media-3683201%402x.png)

By specifying whether your study requires one or more of the sensors, people can opt out, participate partially, or fully opt in. To indicate that your study requires a sensor, add a Boolean key titled `Required` to the sensorʼs usage-detail dictionary with a value of `true`.

```plist
<key>SRSensorUsageMotion</key>
<dict> 
    ... 
    <key>Required</key> 
    <true/>
</dict>
```

For sensor information that’s optional to your study, you can omit the `Required` key or set its value to `false`.

If a person disapproves of a required sensor, the system warns them that the study requires the information. In the prompt, they have the option to not enroll or to reconsider by tapping Change Choice.

![Screenshot of the Research Sensor & Usage Data Request sheet’s second page. A model prompt displays text explaining that a sensor the user disallowed is required for the study, followed by two buttons. The upper button reads “Don’t Enroll in Study”. The lower button reads, “Change Choice”. ](https://docs-assets.developer.apple.com/published/fe9bacde05a71fb8244fb0b0c6d6c4bf/media-3683200%402x.png)

After a person answers the prompt, they can adjust authorization status per sensor later by choosing Settings > Privacy > Research Sensor & Usage Data.

## See Also

- [class SRSensorReader](srsensorreader.md)
  An object that establishes user authorization and records data for a particular sensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading)*