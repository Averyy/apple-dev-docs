# Privacy manifest files

**Framework**: Bundle Resources

Describe the data your app or third-party SDK collects and the reasons required APIs it uses.

#### Overview

Apps and third-party SDKs — distributed as XCFrameworks, Swift packages, or Xcode projects — can contain a privacy manifest file, named `PrivacyInfo.xcprivacy`. The privacy manifest is a property list that records the following information:

- The types of data collected by your app or third-party SDK. You need to provide this information for your app or third-party SDK on all platforms.
- The required reasons APIs your app or third-party SDK uses. You need to provide this information for your app or third-party SDK on iOS, iPadOS, tvOS, visionOS, and watchOS.

For each type of data your app or third-party SDK collects and category of required reasons API it uses, the app or third-party SDK needs to record the reasons in its bundled privacy manifest file.

> ❗ **Important**:  You need to include a privacy manifest file in your third-party SDK if it’s listed in “SDKs that require a privacy manifest and signature,” in [`Upcoming third-party SDK requirements`](https://developer.apple.comhttps://developer.apple.com/support/third-party-SDK-requirements/). Otherwise, include a privacy manifest file in your third-party SDK if it uses required reasons API, collects data about the person using apps that include the third-party SDK, enables the app to collect data about people using the app, or contacts tracking domains. Providing a privacy manifest file helps app developers to understand the API use and data-collection practices of your third-party SDK.

##### Create a Privacy Manifest

To add the privacy manifest to your app or third-party SDK in Xcode, follow these steps:

- Choose File > New File.
- Scroll down to the Resource section, and select App Privacy File type.
- Click Next.
- Check your app or third-party SDK’s target in the Targets list.
- Click Create.

By default, the file is named `PrivacyInfo.xcprivacy`; this is the required file name for bundled privacy manifests.

> **Note**:  You need to add the privacy manifest file to your target’s resources for Xcode to use it when you generate a privacy report. If you distribute your third-party SDK as a static library, use the support for static frameworks in Xcode 15 or later to bundle resources, including the privacy manifest file. Create a framework target in Xcode that builds your product, set its Mach-O type build setting to “Static Library,” and add the privacy manifest file to your target’s bundle resources along with any other resources, for example, image files.

At the top level of this property list file, add the following keys to the dictionary:

To provide a list of internet domains in `NSPrivacyTrackingDomains`, set `NSPrivacyTracking` to `true`.

## Topics

### Essentials
- [Adding a privacy manifest to your app or third-party SDK](adding-a-privacy-manifest-to-your-app-or-third-party-sdk.md)
  Report the data you collect and the required reasons API you use in your app or third-party SDK.
- [Describing data use in privacy manifests](describing-data-use-in-privacy-manifests.md)
  Declare the data collected by your app or by third-party SDKs.
- [Describing use of required reason API](describing-use-of-required-reason-api.md)
  Ensure your use of covered API is consistent with policy.
- [App Privacy Configuration](app-privacy-configuration.md)
  A data structure that represents the root object in a privacy manifest file.

## See Also

- [Entitlements](entitlements.md)
  Key-value pairs that grant an executable permission to use a service or technology.
- [Information Property List](information-property-list.md)
  A resource containing key-value pairs that identify and configure a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files)*