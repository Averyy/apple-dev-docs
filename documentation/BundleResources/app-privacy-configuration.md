# App Privacy Configuration

**Framework**: Bundle Resources  
**Kind**: struct

A data structure that represents the root object in a privacy manifest file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

Use the keys and values in this object in the privacy manifest for your app or third-party SDK. For more information, see [`Privacy manifest files`](privacy-manifest-files.md).

## Topics

### Describing privacy accessed API use
- [NSPrivacyAccessedAPITypes](app-privacy-configuration/nsprivacyaccessedapitypes.md)
  A list of dictionaries that report the privacy accessed API your app or third-party SDK uses.
### Describing collected data
- [NSPrivacyCollectedDataTypes](app-privacy-configuration/nsprivacycollecteddatatypes.md)
  A list of dictionaries that report the categories of private data your app or third-party SDK collects.
### Declaring tracking
- [NSPrivacyTracking](app-privacy-configuration/nsprivacytracking.md)
  A Boolean value that indicates whether your app or third-party SDK uses data for tracking.
- [NSPrivacyTrackingDomains](app-privacy-configuration/nsprivacytrackingdomains.md)
  A list of the internet domains your app or third-party SDK uses for tracking.

## See Also

- [Adding a privacy manifest to your app or third-party SDK](adding-a-privacy-manifest-to-your-app-or-third-party-sdk.md)
  Report the data you collect and the required reasons API you use in your app or third-party SDK.
- [Describing data use in privacy manifests](describing-data-use-in-privacy-manifests.md)
  Declare the data collected by your app or by third-party SDKs.
- [Describing use of required reason API](describing-use-of-required-reason-api.md)
  Ensure your use of covered API is consistent with policy.
- [Editing property list files](../Xcode/editing-property-list-files.md)
  Add, remove, and change keys and values in a structured file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-privacy-configuration)*