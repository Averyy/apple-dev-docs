# Diagnosing Issues with Entitlements

**Framework**: Bundle Resources

Verify your app’s entitlements at every stage of development to track down errors during distribution.

#### Overview

If an error referencing an entitlement occurs during iOS development you can check your entitlements at different stages of your app’s build process to determine where you need to make corrections. Use the following set of steps to find out where you need to fix problems with your entitlements.

##### Enable Necessary Entitlements Only

Before submitting your app for review, limit entitlements to the minimum required for your application to function. Remove any unnecessary entitlements that your app isn’t using. Do this by turning off Capabilities in your Xcode project that your app is not using and by removing unused entitlements from your entitlements file. Depending on what entitlements you are removing, the cleanup involved may be as simple as turning off a Capability in your project or it may involve manually editing your entitlements file or files. In special cases, cleanup may include contacting the group at Apple that worked with you to add specific entitlements to your app.

##### Check Target Capabilities

Adding Capabilities to your Xcode project will sometimes add entries into your project’s entitlements files. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). In those cases, you may need to manually edit your entitlements file after you turn off those Capabilities to remove the corresponding entries from your entitlements file in cases where Xcode is unable to.

In your Capabilities tab, make sure you’ve only enabled the minimum set of capabilities needed for your app to function.

##### Check Your Entitlements Files

Each target in your app may have its own entitlements file. To locate the entitlements file associated with a particular target, look at the the Code Signing Entitlements file setting inside of the Signing settings displayed in your Build Settings. If you see errors in your build log related to an entitlement that you added to one of your entitlements files, check to make sure those entries are correct.

Sometimes, error messages involving entitlements may not be specific. If the an error message references an invalid or malformed entitlement and you’ve manually edited your entitlement file or files, check your entitlements files for incorrect entries.

##### Check Your Provisioning Profile

You can inspect the entitlements associated with your provisioning profile inside of Xcode by clicking the info button (a small, gray disk with a lowercase “i” in the center) next to the Provisioning Profile field in the Signing editor, in your [`developer account`](https://developer.apple.comhttps://developer.apple.com) online, or by downloading your provisioning profile and viewing its contents using a command-line tool in the Terminal.

Every App ID listed in your developer account can have a number of capabilities associated with it and some of those capabilities are paired with entitlements. Compare the capabilities listed for your App ID with the capabilities selected in your app’s Signing & Capabilities tab and the entitlements appearing in your app’s entitlements file or files.

Provisioning profiles have entitlements associated with them.  You can download any of your provisioning profiles from your developer account and inspect its entitlements by running a command-line tool. For example, if you downloaded a provisioning profile named `iOSTeamProfile.mobileprovison`, you’d use the following command to get a list of the entitlements for a provisioning profile:

```sh
% security cms -D -i iOSTeamProfile.mobileprovision | xmllint --xpath "/plist/dict/key[text()='Entitlements']/following-sibling::dict[position()=1]" -

```

When you run this command, the `security` tool returns a `plist` file that describes the entire contents of the provisioning profile and the `xmllint` command runs an `xpath` query to pull out the dictionary that lists the entitlements. In that list you will see all the entitlements specifically encoded in your provisioning profile. For example, here is a sample of output from the command:

```xml
<dict>

<key>application-identifier</key>
<string>Z3P45X123C.*</string>

<key>keychain-access-groups</key>
<array>
<string>Z3P45X123C.*</string>
</array>

<key>get-task-allow</key>
<true/>

<key>com.apple.developer.sample</key>
<string>Z3P45X123C</string>

</dict>
```

##### Check the Entitlements in Your Build Log and App

Verify that Xcode is using the provisioning profile you expect when building your app by inspecting the signing step in your build log. You’ll find the name of the provisioning profile Xcode used to sign your app in the invocation of the `codesign` tool’s command-line parameters.

Once you’ve build your app, inspect the entitlements built into your app by running the following command in the terminal:

```sh
% codesign --display --entitlements :- YourApp.app
```

This command prints a `plist` that contains all of the entitlements built into the app.

##### Check the Entitlements When Submitting Your App

When you submit your app to Apple, Xcode displays a list of entitlements associated with your app in the confirmation window for uploading your app. Verify that all of the entitlements shown are consistent with the entitlements you’ve selected in your project.

##### Fix Installation Failure Entitlement Issues

You can remove following entitlements from your entitlements file if they are present and cause an error during installation. These may be present in older projects for legacy reasons.

1. `application-identifier`; this entitlement is defined by the provisioning profile instead.
2. `get-task-allow`; this entitlement is defined by the provisioning profile instead.

If you receive the error message “Upgrade’s application-identifier entitlement string [….] does not match installed application’s application-identifier string [….]; rejecting upgrade.” and you’ve changed your application’s id, then you need to add a previous-application-identifiers entitlement to your provisioning profile. Contact Apple Developer programs for assistance using your account’s Developer Contact page > Membership > Enrollment and Account > Apple Developer Program Support form.

##### Fix Problems with Special Entitlements

If you received authorization to use a specific entitlement from a group at Apple and you’re having difficulty with that entitlement, contact that group for troubleshooting assistance.

## See Also

- [Adding capabilities to your app](../Xcode/adding-capabilities-to-your-app.md)
  Configure your target to include and customize capabilities that provide access to Apple’s app services.
- [Signing a daemon with a restricted entitlement](../Xcode/signing-a-daemon-with-a-restricted-entitlement.md)
  Wrap a daemon in an app-like structure to use an entitlement thatʼs authorized by a provisioning profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/diagnosing-issues-with-entitlements)*