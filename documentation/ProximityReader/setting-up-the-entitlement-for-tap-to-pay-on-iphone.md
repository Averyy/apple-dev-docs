# Setting up Tap to Pay on iPhone

**Framework**: ProximityReader

Request and configure the required entitlement to support Tap to Pay on iPhone.

#### Overview

Tap to Pay on iPhone lets merchants accept contactless payments using an app on their iPhone, without having to connect external hardware. Your app uses the [`ProximityReader`](ProximityReader.md) framework to read the payment method someone presents.

To integrate with ProximityReader and use Tap to Pay on iPhone, you need to request the [`Tap to Pay on iPhone Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/tap-to-pay-on-iphone/). To access the request form, you need to have an organization-level Apple Developer account and be logged in as the Account Holder. Apple reviews each application using predefined criteria. If your request meets the criteria, Apple adds the entitlement to your developer account using managed capabilities. For more information, see [`Provisioning with capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities).

After you receive the entitlement, you need to configure your Xcode project to use it, which involves several steps. You create or update an App ID, generate a provisioning profile, and add the entitlement to the `Info.plist` file for your target. Your project’s code signing settings might also require minor changes.

> **Note**: TestFlight beta testing and App Store submissions require an entitlement that allows distribution. If you’ve already completed your testing with the nondistribution entitlement, respond to the original email and rerequest the [`Tap to Pay on iPhone Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/tap-to-pay-on-iphone/).

TestFlight beta testing and App Store submissions require an entitlement that allows distribution. If you’ve already completed your testing with the nondistribution entitlement, respond to the original email and rerequest the [`Tap to Pay on iPhone Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/tap-to-pay-on-iphone/).

##### Add the Tap to Pay on Iphone Capability to Your App Id

Follow these steps to update your App ID to include the necessary capability:

1. Create an App ID for your app if you don’t already have one. For more information, see [`Register an App ID`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-identifiers/register-an-app-id).
2. Sign in to your [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account/) account and select Certificates, IDs & Profiles.
3. Select Identifiers in the menu on the left.
4. Select your app from the list.
5. Click the Additional Capabilities tab.
6. Enable the Tap to Pay on iPhone capability.
7. Click the Save button.
8. Create a new provisioning profile for the updated App ID. For more information, see [`Create a development provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-profiles/create-a-development-provisioning-profile).

##### Download the New Provisioning Profile

> 💡 **Tip**: You can skip these steps if you enable Xcode to automatically manage the code signing. For more information, see [`Automatic Signing Controls`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-your-team/automatic-signing-controls/).

You can skip these steps if you enable Xcode to automatically manage the code signing. For more information, see [`Automatic Signing Controls`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-your-team/automatic-signing-controls/).

Follow these steps to use the new provisioning profile to code sign your app:

1. In Xcode, select your project in the Project navigator.
2. In the project editor, click the Signing & Capabilities tab.
3. Click All in the scope bar, and then deselect “Automatically manage signing”.
4. Click the Provisioning Profile pop-up menu and choose Download Profile.
5. Select your ProximityReader provisioning profile from the left column and click Select Profile.

##### Add an Entitlements File

In Xcode, you need to create a file to specify the entitlements necessary for your app to use Tap to Pay on iPhone.

> 💡 **Tip**: Xcode might create a `.entitlements` file for you. In that case, just add `com.apple.developer.proximity-reader.payment.acceptance` as a Boolean value to that file.

Xcode might create a `.entitlements` file for you. In that case, just add `com.apple.developer.proximity-reader.payment.acceptance` as a Boolean value to that file.

To create the entitlements file:

1. In Xcode, select your project in the Project navigator.
2. Choose File > New > File from Template, select Property List from the Resource section, and click Next.
3. Enter `your_project.entitlements` as the filename, replacing `your_project` with the name of your project, and click Create.
4. In the project editor, click the Build Settings tab.
5. Click All and Combined in the scope bar.
6. Use the search box to find the Code Signing Entitlements setting.
7. Enter the full path to the `.entitlements` file from step 3 as the setting’s value.
8. Open the file in Xcode and add `com.apple.developer.proximity-reader.payment.acceptance` as a Boolean value.

The following example shows the contents of an app’s `.entitlements` file with the Tap to Pay on iPhone capability:

```xml
<key>com.apple.developer.proximity-reader.payment.acceptance</key>
<true/>
```

## See Also

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)
  Configure your app to use Tap to Pay on iPhone to read contactless payment cards.
- [class PaymentCardReader](paymentcardreader.md)
  An object you use to configure Tap to Pay on iPhone on the current device.
- [class PaymentCardReaderSession](paymentcardreadersession.md)
  The object you use to start reading a contactless payment or loyalty card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone)*