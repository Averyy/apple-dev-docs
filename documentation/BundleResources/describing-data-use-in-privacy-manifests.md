# Describing data use in privacy manifests

**Framework**: Bundle Resources

Declare the data collected by your app or by third-party SDKs.

#### Overview

Record the categories of data that your app or third-party SDK collects about the person using the app, and the reasons it collects the data. App developers can use Xcode to create a privacy report, summarizing the information about collected data in their app and the third-party SDKs the app links to.

> ❗ **Important**:  Third-party SDKs need to provide their own privacy manifest files that record the types of data they collect. Your app’s privacy manifest file doesn’t need to cover data collected by third-party SDKs that your app links to.

 Third-party SDKs need to provide their own privacy manifest files that record the types of data they collect. Your app’s privacy manifest file doesn’t need to cover data collected by third-party SDKs that your app links to.

##### Describe the Data Your App or Third Party Sdk Collects

For each type of data your app or third-party SDK collects, add a dictionary to the [`NSPrivacyCollectedDataTypes`](app-privacy-configuration/nsprivacycollecteddatatypes.md) array in your privacy information file. Add the following keys to the dictionary.

Xcode won’t generate a privacy report correctly if you define your own collected data types for the `NSPrivacyCollectedDataType` key, or provide your own reasons for the `NSPrivacyCollectedDataTypePurposes` key. Use values listed in the documentation for the keys.

##### Create Your Apps Privacy Report

Xcode can create a privacy report by aggregating the privacy manifests from your app and the third-party SDKs it links to. Use the privacy report to better understand all of the data collected by your app and whether it tracks. Create the privacy report for your app by doing the following:

1. Open your project in Xcode.
2. Choose Product > Archive. Xcode creates the archive and reveals it in the organizer.
3. Control-click the archive in the organizer and choose Generate Privacy Report.
4. Choose a location to save the privacy report.
5. Switch to Finder.
6. Navigate to the location where you saved the privacy report, and double-click to open the report in Preview.

The privacy report is organized in a similar way to Privacy Nutrition Labels. Refer to this report when you provide your app’s privacy details in App Store Connect. For more information on providing your app’s privacy details, see [`App privacy details on the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/app-privacy-details/).

## See Also

- [Adding a privacy manifest to your app or third-party SDK](adding-a-privacy-manifest-to-your-app-or-third-party-sdk.md)
  Report the data you collect and the required reasons API you use in your app or third-party SDK.
- [Describing use of required reason API](describing-use-of-required-reason-api.md)
  Ensure your use of covered API is consistent with policy.
- [App Privacy Configuration](app-privacy-configuration.md)
  A data structure that represents the root object in a privacy manifest file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests)*