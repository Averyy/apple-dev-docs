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
- [Read the app clip domain cache status information for a build bundle](get-v1-buildbundles-_id_-appclipdomaincachestatus.md)
  Get the cache status of the domain you associate with your App Clip for a specific build bundle.
- [Read app clip domain debug status information for a build bundle](get-v1-buildbundles-_id_-appclipdomaindebugstatus.md)
  Get the debug status of the domain you associate with your App Clip for a specific build bundle.
- [List all beta app clip invocations for a build bundle](get-v1-buildbundles-_id_-betaappclipinvocations.md)
  Get all App Clip invocations you configure for testing for a specific build bundle.
- [List all file sizes for a build bundle](get-v1-buildbundles-_id_-buildbundlefilesizes.md)
  Get all file sizes for a specific build bundle.
- [Get the App Clip domain cache status ID for a build bundle](get-v1-buildbundles-_id_-relationships-appclipdomaincachestatus.md)
- [Get the App Clip domain debug status ID for a build bundle](get-v1-buildbundles-_id_-relationships-appclipdomaindebugstatus.md)
- [List beta App Clip invocation IDs for a build bundle](get-v1-buildbundles-_id_-relationships-betaappclipinvocations.md)
- [List file size IDs for a build bundle](get-v1-buildbundles-_id_-relationships-buildbundlefilesizes.md)
### Objects
- [object BuildBundle](buildbundle.md)
  A specific binary bundle within a build, such as an app extension, App Clip, or nested app target.
- [type BuildBundleType](buildbundletype.md)
  A string that represents the possible components of a build bundle.
- [object AppClipDomainStatus](appclipdomainstatus.md)
  The validation status of the associated domains configured for an App Clip, indicating whether each domain is reachable and correctly set up.
- [object BuildBundleFileSize](buildbundlefilesize.md)
  The estimated and actual download and install sizes for a build bundle, broken down by device type.
- [object AppClipDomainStatusResponse](appclipdomainstatusresponse.md)
  A response containing the validation status of associated domains configured for an App Clip.
- [object BetaAppClipInvocationsResponse](betaappclipinvocationsresponse.md)
  A response containing a list of TestFlight App Clip invocations for a beta build.
- [object BuildBundleFileSizesResponse](buildbundlefilesizesresponse.md)
  A response containing a list of download and install size estimates for a build’s bundles.

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Icons](build-icons.md)
  Get icons from your app’s binary that are uploaded to App Store.
- [Build uploads](build-uploads.md)
  Read metadata for app builds you upload to App Store Connect.
- [App Encryption Declarations](app-encryption-declarations.md)
  View, and assign to builds, the declarations about types of encryption used in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-bundles)*