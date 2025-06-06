# Build Bundles

**Framework**: App Store Connect API

Read metadata for app and App Clip binaries included in a build you upload to App Store Connect.

#### Overview

A `buildBundles` resource represents metadata for binaries you upload to App Store Connect as a build. It provides detailed information like capabilities an app uses, supported CPU architectures, and more. For a full list of available attributes, see [`BuildBundle.Attributes`](buildbundle/attributes-data.dictionary.md).

When you upload a build that contains an App Clip, use the APIs provided by the `buildBundles` resource to read:

- Cache status information for domains you associated with your App Clip
- Debug status information for domains you associated with your App Clip
- App Clip invocations you configured for testers who use the TestFlight app to launch your App Clip
- File size information for a build bundle

## Topics

### Getting Build Bundle Information
- [Read the App Clip Domain Cache Status Information for a Build Bundle](get-v1-buildbundles-_id_-appclipdomaincachestatus.md)
  Get the cache status of the domain you associate with your App Clip for a specific build bundle.
- [Read App Clip Domain Debug Status Information for a Build Bundle](get-v1-buildbundles-_id_-appclipdomaindebugstatus.md)
  Get the debug status of the domain you associate with your App Clip for a specific build bundle.
- [List All Beta App Clip Invocations for a Build Bundle](get-v1-buildbundles-_id_-betaappclipinvocations.md)
  Get all App Clip invocations you configure for testing for a specific build bundle.
- [List All File Sizes for a Build Bundle](get-v1-buildbundles-_id_-buildbundlefilesizes.md)
  Get all file sizes for a specific build bundle.
### Objects
- [object BuildBundle](buildbundle.md)
  The data structure that represents Build Bundles resource.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The data structure that represents the App Clip Domain Statuses resource.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The data structure that represents a Build Bundle File Sizes resource.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response that contains a single App Clip Domain Statuses resource.
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response that contains a list of Beta App Clip Invocations resources.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response that contains a list of Build Bundle File Sizes resources.

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Icons](build-icons.md)
  Get icons from your app’s binary that are uploaded to App Store.
- [App Encryption Declarations](app-encryption-declarations.md)
  View, and assign to builds, the declarations about types of encryption used in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-bundles)*