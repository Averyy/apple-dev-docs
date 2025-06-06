# Build Icons

**Framework**: App Store Connect API

Get icons from your app’s binary that are uploaded to App Store.

#### Overview

Use `buildIcons` to identify which icons were uploaded to App Store Connect inside your app’s binary. This is a read-only resource. For a list of supported icon asset types, see [`IconAssetType`](iconassettype.md).

## Topics

### Getting Metadata and Downloading Icons
- [List All Icons for a Build](get-v1-builds-_id_-icons.md)
  List all the icons for various platforms delivered with a build.
### Objects and Types
- [object BuildIcon](buildicon.md)
  The data structure that represents the Build Icons resource.
- [object BuildIconsResponse](buildiconsresponse.md)
  A response that contains a list of Build Icon resources.
- [object BuildIconsWithoutIncludesResponse](buildiconswithoutincludesresponse.md)
- [object ImageAsset](imageasset.md)
  An image asset, including its height, width, and template URL.
- [type IconAssetType](iconassettype.md)
  String that represents the type of icon contained in the build.

## See Also

- [Builds](builds.md)
  Manage builds for testers and submit builds for review.
- [Build Bundles](build-bundles.md)
  Read metadata for app and App Clip binaries included in a build you upload to App Store Connect.
- [App Encryption Declarations](app-encryption-declarations.md)
  View, and assign to builds, the declarations about types of encryption used in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/build-icons)*